import logging
import os
import pickle
import re
import time
from contextlib import contextmanager
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import \
    LOGGER as selenium_logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tqdm.auto import tqdm
from utils import utilize_loggers
from webdriver_manager.chrome import ChromeDriverManager

selenium_logger.setLevel(logging.WARNING)
os.environ["WDM_LOG"] = "0"


@contextmanager
def timer():
    t0 = time.time()
    yield lambda: time.time() - t0


def measure_elapsed_time(timer_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with timer() as elapsed_time:
                result = func(*args, **kwargs)
                logger.info(f"{elapsed_time():>8.3f} seconds elapsed @ {timer_name}")
            return result

        return wrapper

    return decorator


class QADataCrawler:
    def __init__(
        self,
        board_url="https://www.klac.or.kr/legalstruct/cyberConsultation/selectOpenArticleList.do?boardCode=3#none",
        base_url="https://www.klac.or.kr/legalstruct/cyberConsultation/selectOpenArticleDetail.do?boardCode=3&contentId=",
    ):
        self.driver = None
        self.board_url = board_url
        self.base_url = base_url

    def start_driver(self):
        self.chrome_service = webdriver.chrome.service.Service(
            ChromeDriverManager().install()
        )
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("headless")

        self.driver = webdriver.Chrome(
            service=self.chrome_service,
            options=self.chrome_options,
        )

        self.chrome_service.start()

    def quit_driver(self):
        self.driver.quit()

    @measure_elapsed_time("Total Crawling Process")
    def get_data(self):
        case_ids = self._get_all_case_ids()
        case_info = self._get_all_case_contents(case_ids)

        self._save_dataframe(case_info)

    def _get_case_id(self):
        case_ids = []
        element_xpath = "//a[contains(@onclick, 'fn_inquire_detail')]"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, element_xpath))
        )
        elements = self.driver.find_elements(By.XPATH, element_xpath)
        for element in elements:
            match = re.search(
                r"fn_inquire_detail\('(\d+)', '(.*?)'\);return false;",
                element.get_attribute("onclick"),
            )
            case_ids.append(match.group(2))
        return case_ids

    @measure_elapsed_time("Get all case ids")
    def _get_all_case_ids(self, save_id_list=False):
        is_crawling_finished = False
        page_move_cnt = 0
        page_number = 1
        page_idx = 2
        case_ids = []

        self.driver.get(self.board_url)
        case_ids.extend(self._get_case_id())

        while not is_crawling_finished:
            try:
                next_page = self.driver.find_element(
                    By.XPATH,
                    f'//*[@id="content"]/form[1]/div[2]/div/div[4]/a[{page_idx}]',
                )
                page_idx += 1
            except:
                try:
                    next_page = self.driver.find_element(
                        By.XPATH,
                        f'//button[contains(@onclick, "fn_select_linkPage({page_move_cnt * 10 + page_idx}); return false;")]',
                    )
                    page_idx = 2
                    page_move_cnt += 1
                except:
                    is_crawling_finished = True
                    break

            next_page.click()
            case_ids.extend(self._get_case_id())
            page_number += 1

            if save_id_list:
                self._save_case_id_list(case_ids, "case_id_list.pkl")

        return case_ids

    def _get_case_content_by_id(self, case_id):
        url = self.base_url + case_id
        html = urlopen(url)
        bsObject = BeautifulSoup(html, "html.parser")

        case_title = bsObject.find("div", {"class": "view_head"}).text
        date_created = bsObject.find("dt", text="신청일").find_next_sibling("dd").text
        date_answered = bsObject.find("dt", text="답변일자").find_next_sibling("dd").text
        content, answer = bsObject.find_all("div", {"class": "notice_contents"})
        case_info = [case_title, date_created, date_answered, content.text, answer.text]

        return case_info

    @measure_elapsed_time("Get all case contents")
    def _get_all_case_contents(self, case_ids):
        case_info = []

        for case_id in tqdm(case_ids):
            case_info.append(self._get_case_content_by_id(case_id))

        return case_info

    def _save_dataframe(self, case_info, drop_unused_columns=False):
        df = pd.DataFrame(
            case_info,
            columns=[
                "case_title",
                "date_created",
                "date_answered",
                "content",
                "answer",
            ],
        )

        if drop_unused_columns:
            df = df.drop(["case_title", "date_created", "date_answered"], axis=1)

        os.makedirs("data", exist_ok=True)
        df.to_csv("./data/raw_qa_dataset.csv", index=False)
        logger.info(f"\t\tGathered Data Count: {len(df)}")

    def _save_case_id_list(self, case_id_list, file_name="case_id_list.pkl"):
        with open(file_name, "wb") as f:
            pickle.dump(case_id_list, f)

    def _load_case_id_list(self, file="case_id_list.pkl"):
        with open(file, "rb") as f:
            loaded_list = pickle.load(f)
        return loaded_list


if __name__ == "__main__":
    logger = utilize_loggers(__file__)

    crawler = QADataCrawler()
    crawler.start_driver()
    crawler.get_data()
    crawler.quit_driver()
