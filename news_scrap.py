import random
import time
from bs4 import BeautifulSoup
import requests
from models import News

def get_news_links():
    news_list = []
    url = f'https://www.investing.com/news/'
    r = requests.get(url)
    content = r.text

    soup = BeautifulSoup(content, 'html.parser')  # vparsavt

    news_box = soup.find('div',{'id':"latestNews"})
    all_news = news_box.find_all('a',{'class':"title"})
    for a in all_news:
        href = a.get('href')
        news_list.append(href)
    print(news_list)
    return news_list
def get_news(links_list):
    whole_news_list = []

    for link in links_list:
        try:
            time.sleep(random.randint(8, 15))
            text = ''
            article = f'https://www.investing.com{link}'
            r = requests.get(article)
            content = r.text
            soup = BeautifulSoup(content, 'html.parser')  # vparsavt
            article_box = soup.find('div',{'class':'WYSIWYG articlePage'})
            all_paragraphs = article_box.find_all('p')
            for p in all_paragraphs:
                text += p.text
            name = soup.find('h1',{'class':'articleHeader'}).text
            news_obj = News(name=name, text=text)
            whole_news_list.append(news_obj)
            print(name)
        except:
            continue
    return whole_news_list





