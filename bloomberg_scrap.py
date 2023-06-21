# import os
# os.system('pip install selenium')
# os.system('pip install chromedriver-binary==114.0.5735.90.0')#an 114
import requests
import time
from random import randint
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument("window-size=1920,1080")  # ase dayeneba schirdeba rom ekranze ar gaxsnas saiti da
# konkretuli zomebi mieces rom info wamoigos
wd = webdriver.Chrome(options=options)
wd.implicitly_wait(15)


url = "https://www.bloomberg.com/markets/stocks"

wd.get(url)  # aq saiti chairtveba
elem = WebDriverWait(wd, 15).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="navi-bar"]/a/img[1]'))
    # This is a dummy element
)  # velodebit bolomde chatvirtvas
time.sleep(2)

content = wd.page_source
soup = BeautifulSoup(content, 'html.parser')  # vparsavt

first_table = soup.find('div',{"class":'data-tables first'})
print(first_table)
# other_tables = soup.find_all('div',{"class":'data-tables'})
# table_rows_first = first_table.find_all('tr',{"class":"data-table-row"})
# for tr in table_rows_first:
#     value = tr.find('td',{'class':'data-table-row-cell'}).find('span',{'class':"data-table-row-cell__value"}).text
#     print(value)