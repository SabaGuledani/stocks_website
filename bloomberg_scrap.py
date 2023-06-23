# import os
# os.system('pip install selenium')
# os.system('pip install chromedriver-binary==114.0.5735.90.0')#an 114
import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from models import db, Global_funds



def get_bloomberg_data():
    bloomberg_list = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("window-size=1920,1080")
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(5)

    url = "https://www.bloomberg.com/markets/stocks"

    wd.get(url)  # aq saiti chairtveba
    elem = WebDriverWait(wd, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="navi-bar"]/a/img[1]'))
        # This is a dummy element
    )  # velodebit bolomde chatvirtvas
    time.sleep(2)

    content = wd.page_source
    soup = BeautifulSoup(content, 'html.parser')  # vparsavt

    other_tables = soup.find_all('div', {"class": 'data-tables'})
    i = 0
    for table in other_tables:
        table_rows = table.find_all('tr', {"class": "data-table-row"})
        for tr in table_rows:
            if i == 0:
                header = "us"
            elif i == 1:
                header = "eu"
            elif i == 2:
                header = 'asia'
            all_td = tr.find_all('td', {'class': 'data-table-row-cell'})
            row_values_list = []
            name = (tr.find('th').find('a').find_all('div')[1]).text
            for td in all_td:
                value = td.find('span', {'class': "data-table-row-cell__value"}).text
                row_values_list.append(value)
            fund = Global_funds(name=name, value=row_values_list[0],
                                net_change=row_values_list[1], percent_change=row_values_list[2],
                                month_change=row_values_list[3], header=header)
            bloomberg_list.append(fund)
            # with app.app_context():
            #     db.session.add(fund)
            #     db.session.commit()
            #     print(f'damatda {name}')
        i += 1
    return bloomberg_list
