import pickle
import re
import time
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tqdm.auto import tqdm
from webdriver_manager.chrome import ChromeDriverManager


def get_case_id(driver):
    case_ids = []
    element_xpath = "//a[contains(@onclick, 'fn_inquire_detail')]"
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, element_xpath))
    )
    elements = driver.find_elements(By.XPATH, element_xpath)
    for element in elements:
        match = re.search(
            r"fn_inquire_detail\('(\d+)', '(.*?)'\);return false;",
            element.get_attribute("onclick"),
        )
        case_ids.append(match.group(2))
    return case_ids


def save_case_id_list(case_id_list, file_name="case_id_list.pkl"):
    with open(file_name, "wb") as f:
        pickle.dump(case_id_list, f)


def load_case_id_list(file="case_id_list.pkl"):
    with open(file, "rb") as f:
        loaded_list = pickle.load(f)
    return loaded_list


def get_case_info_by_id(base_url, id):
    url = base_url + id
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")

    case_title = bsObject.find("div", {"class": "view_head"}).text
    date_created = bsObject.find("dt", text="신청일").find_next_sibling("dd").text
    date_answered = bsObject.find("dt", text="답변일자").find_next_sibling("dd").text
    content, answer = bsObject.find_all("div", {"class": "notice_contents"})
    case_info = [case_title, date_created, date_answered, content.text, answer.text]

    return case_info


def main():
    board_url = "https://www.klac.or.kr/legalstruct/cyberConsultation/selectOpenArticleList.do?boardCode=3#none"
    base_url = "https://www.klac.or.kr/legalstruct/cyberConsultation/selectOpenArticleDetail.do?boardCode=3&contentId="

    chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    chrome_service.start()
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    driver.get(board_url)

    case_id_list = []
    case_id_list.extend(get_case_id(driver))

    page_number = 1
    print(f"Crawling of page {page_number} is finished.")

    page_idx = 2
    page_move_cnt = 0

    while True:
        # test
        if page_move_cnt == 1: break
        try:
            next_page = driver.find_element(
                By.XPATH, f'//*[@id="content"]/form[1]/div[2]/div/div[4]/a[{page_idx}]'
            )
            page_idx += 1
        except:
            try:
                next_page = driver.find_element(
                    By.XPATH,
                    f'//button[contains(@onclick, "fn_select_linkPage({page_move_cnt * 10 + page_idx}); return false;")]',
                )
                page_idx = 2
                page_move_cnt += 1
            except:
                print("Crawling Finished.")
                break

        next_page.click()
        case_id_list.extend(get_case_id(driver))
        page_number += 1
        print(f"Crawling of page {page_number} is finished.")

    save_case_id_list(case_id_list, "case_id_list.pkl")

    driver.quit()

    case_info = []
    for case_id in tqdm(case_id_list):
        case_info.append(get_case_info_by_id(base_url, case_id))

    df = pd.DataFrame(case_info, columns=["case_title", "date_created", "date_answered", "content", "answer"])
    df.to_csv("raw_qa_dataset.csv", index=False)

if __name__ == "__main__":
    main()
