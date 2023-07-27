from tqdm import trange
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

def set_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    return options

def wait_driver_click(id):
    WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.ID, id))
    driver.find_element(By.ID, id).click()


def spell_check(txt, delay = 15):
    if len(txt) > 1200:
        return ''
    
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, 'character_counter_content'))
    driver.find_element(By.ID, 'character_counter_content').send_keys(txt)
 
    wait_driver_click('spell_check')
    driver.implicitly_wait(delay)
    wait_driver_click('spell_done_all')
    driver.implicitly_wait(1)

    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CSS_SELECTOR, '#checker_preview'))
    clean_txt = driver.find_element(By.CSS_SELECTOR, '#checker_preview').text
    driver.refresh()
    return clean_txt


dt = pd.read_csv('preprocessed_qa_spacing_pre_word.csv')
new_q = []
new_a = []
options = set_options()

# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument('--no-sandbox')
# options.add_argument("--single-process")
# options.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.get('https://www.saramin.co.kr/zf_user/tools/character-counter')

q_v = dt['question'].values
a_v = dt['answer'].values

for i in trange(len(dt)):
    if len(q_v[i]) > 1200:
        continue
    try:
        new_q.append(spell_check(q_v[i]))
        new_a.append(a_v[i])
    except:
        continue

driver.quit()


clean_data = pd.DataFrame({'question' : new_q, 'answer' :new_a})

clean_data.to_csv('preprocessed_qa_spacing_spell.csv', index=False)