import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_popular_stocks():
    ticker_list = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("window-size=1920,1080")
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(5)

    url = "https://finance.yahoo.com/most-active"

    wd.get(url)  # aq saiti chairtveba
    elem = WebDriverWait(wd, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="header-logo"]'))
        # This is a dummy element
    )  # velodebit bolomde chatvirtvas
    time.sleep(2)

    content = wd.page_source
    soup = BeautifulSoup(content, 'html.parser')  # vparsavt

    table = soup.find('div', {"class":"Ovx(a) Ovx(h)--print Ovy(h) W(100%)"}).find("tbody")
    all_table_rows = table.find_all('tr')
    for tr in all_table_rows:
        td = tr.find('td')
        ticker = td.find('a').text
        ticker_list.append(ticker)
    return ticker_list
