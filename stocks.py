import sqlite3
import time

import requests
import json
from datetime import date
from datetime import timedelta

from models import db,Stocks,Currency

today = date.today()
date = today - timedelta(days=1)

apikey = 'WI1GOdsaBMaVnImCyZqgHc__H70kDtJ5'


def get_info(tickers, date=date):
    stocks_list = []
    counter = 0
    for ticker in tickers:
        if counter%5 ==0 and counter!=0:
            time.sleep(56)
        url = f'https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey={apikey}'
        url2 = f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={apikey}'

        request_open_close = requests.get(url)
        request_ticker_info = requests.get(url2)

        open_close_res = json.loads(request_open_close.text)
        #
        info_res = json.loads(request_ticker_info.text)




        name = info_res["results"]["name"]
        try:
            desc = info_res["results"]["sic_description"]
        except:
            desc="???"
        stock_open = open_close_res['open']
        close = open_close_res['close']
        high = open_close_res['high']
        low = open_close_res['low']
        after_hours = open_close_res["afterHours"]

        print(name)

        stock_obj = Stocks(symbol=ticker, name=name, description=desc, open=stock_open,
                           close=close, high=high, low=low, after_hours=after_hours, date=date)
        stocks_list.append(stock_obj)
        counter+=1
    return stocks_list
def get_currency(curr_list):
    currency_list = []
    counter = 0
    for curr in curr_list:
        if counter % 5 == 0 and counter != 0:
            time.sleep(56)
        url = f'https://api.polygon.io/v2/aggs/ticker/{"C:"+curr}/prev?adjusted=true&apiKey={apikey}'

        request_open_close = requests.get(url)

        open_close_res = json.loads(request_open_close.text)
        print(open_close_res)
        name = open_close_res["results"][0]["T"]
        close = open_close_res["results"][0]["o"]

        curr_obj = Currency(name=name,close=close,date=today)
        currency_list.append(curr_obj)
        counter += 1
    return currency_list


