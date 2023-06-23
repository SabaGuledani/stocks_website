import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from models import db, Global_funds
import requests

import requests
url = 'https://www.investing.com/news/stock-market-news/us-stocks-are-falling-after-powells-hawkish-rate-outlook-3112100'
r = requests.get(url)
print(r) # დაბეჭდავს <Response [200]>
print(r.status_code) # დაბეჭდავს 200
content = r.text
soup = BeautifulSoup(content, 'html.parser')  # vparsavt
all_paragraphs = soup.find_all('p')


#
#
# def get_news_links():
#     news_list = []
#     options = webdriver.ChromeOptions()
#     # options.add_argument('--headless')
#     options.add_argument("window-size=1920,1080")
#     wd = webdriver.Chrome(options=options)
#     wd.implicitly_wait(5)
#     url = "https://www.investing.com/news/?utm_source=google&utm_medium=cpc&utm_campaign=18539095572&utm_content=626937626563&utm_term=dsa-1463805041937_&GL_Ad_ID=626937626563&GL_Campaign_ID=18539095572&gclid=CjwKCAjwhdWkBhBZEiwA1ibLmFrLDS6W0ka8glTSXkoPP5JRFtVyQK9bcOD0KUtiicfJQ4GIfiCr6xoCAL0QAvD_BwE"
#
#     wd.get(url)  # aq saiti chairtveba
#     time.sleep(2)
#
#     elem = WebDriverWait(wd, 15).until(
#         EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/header'))
#         # This is a dummy element
#     )  # velodebit bolomde chatvirtvas
#
#
#
#     content = wd.page_source
#     soup = BeautifulSoup(content, 'html.parser')  # vparsavt
#
#     news_box = soup.find('div',{'id':"latestNews"})
#     all_news = news_box.find_all('a',{'class':"title"})
#     for a in all_news:
#         href = a.get('href')
#         news_list.append(href)
#
# def get_news(links_list):
#     for link in links_list:
#         article = f'https://www.investing.com/{link}'
#
# get_news_links()
