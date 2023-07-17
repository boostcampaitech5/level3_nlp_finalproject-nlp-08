import os
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class QALawCrawler:
    def __init__(self, start_url="https://www.klac.or.kr/legalinfo/counsel.do"):
        self.start_url = start_url
        self.driver = None

    def give_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--single-process")
        options.add_argument("--disable-dev-shm-usage")
        return options

    def start_driver(self):
        self.driver = webdriver.Chrome(options=self.give_options())

    def quit_driver(self):
        self.driver.quit()

    def crawlling_data(self):
        self.driver.get(self.start_url)

        data_list = []
        end_point = 0

        while end_point == 0:
            for j in range(2, 11):
                for k in range(1, 11):
                    
                    try:
                        self._wait_driver_click(
                            f'//*[@id="content"]/div[2]/div/form/div[2]/table/tbody/tr[{k}]/td[2]/a'
                        )
                        data_list.append(self._collect_data())
                        self._wait_driver_click(f'//*[@id="content"]/div[2]/div/div/a')
                    except:
                        break
                
                try:
                    self._wait_driver_click(
                        f'//*[@id="content"]/div[2]/div/form/div[3]/a[{j}]'
                    )
                except:
                    end_point = 1
                    break
            
            try:
                self._wait_driver_click(
                    '//*[@id="content"]/div[2]/div/form/div[3]/button[3]'
                )
            except:
                break

        self._save_data(data_list=data_list, drop_unused_columns=True)

    def _wait_driver_click(self, xpath):
        WebDriverWait(self.driver, timeout=10).until(
            lambda d: d.find_element(By.XPATH, xpath)
        )
        self.driver.find_element(By.XPATH, xpath).click()

    def _collect_data(self):
        try:
            url = self.driver.current_url
            page_url = urlopen(url)
            soup = bs(page_url, "html.parser")
            data = []
            for i in range(1, 5):
                find_data = soup.select_one(
                    "#print_page > div:nth-child(" + str(i) + ") > dl > dd"
                ).text
                data.append(find_data)
            data.append(url)
            return data
        except:
            return ["error", 0, 0, 0, 0]

    def _save_data(self, data_list, drop_unused_columns=False):
        df = pd.DataFrame(
            data=data_list, columns=["division", "title", "question", "answer", "url"]
        )
        if drop_unused_columns:
            question = df["question"].values.tolist()
            answer = df["answer"].values.tolist()
            df = pd.DataFrame({"question": question, "answer": answer})

        os.makedirs("data", exist_ok=True)
        df.to_csv("./data/law_qa.csv", index=False)


if __name__ == "__main__":
    qa_crawler = QALawCrawler()
    qa_crawler.start_driver()
    qa_crawler.crawlling_data()
    qa_crawler.quit_driver()
