from flask import Flask, redirect, url_for, render_template, json,request,flash
from flask_caching import Cache
from models import db, Global_funds,Stocks,News,Currency
from apscheduler.schedulers.background import BackgroundScheduler
from stocks import get_info,get_currency
from bloomberg_scrap import get_bloomberg_data
from yahoo_finance import get_popular_stocks
from news_scrap import get_news,get_news_links
from datetime import date
from datetime import timedelta
import datetime



today = date.today()
yesterday = today - timedelta(days=1)
yesterday2 = today - timedelta(days=2)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GlobalFunds.sqlite'
cache = Cache(app, config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 86400})  # Set cache timeout to 24 hours

#Secret Key
app.secret_key = 'ShshshItsasecret'

def scrape_data():
    # main_bloomberg_data = get_bloomberg_data()
    # for fund in main_bloomberg_data:
    #     with app.app_context():
    #         db.session.add(fund)
    #         db.session.commit()
    #         print(f'damatda {fund.name}')

    # popular_stocks = get_popular_stocks()
    # print(popular_stocks)
    # all_stocks_info = get_info(popular_stocks)
    # for stock in all_stocks_info:
    #     with app.app_context():
    #         db.session.add(stock)
    #         db.session.commit()
    #         print(f'damatda {stock.symbol}')
    #

    all_curr_info = ["EURUSD",'USDJPY','GBPUSD','AUDUSD','USDCAD']
    all_curr = get_currency(all_curr_info)
    for curr in all_curr:
        with app.app_context():
            db.session.add(curr)
            db.session.commit()
            print(f'damatda {curr.name}')

    # news_links = get_news_links()
    # news = get_news(news_links)
    # for n in news:
    #     with app.app_context():
    #         db.session.add(n)
    #         db.session.commit()
    #         print(f'damatda news')



scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(scrape_data, 'cron', hour=6)  # Schedule the scraping task to run at 00:00 (midnight) each day
date = datetime.date.today().strftime("%B %d, %Y")
subhead = f'Tbilisi, Tuesday morning, {date}'



db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
@cache.cached()
def home():
    data = cache.get('data')
    if data:
        stocks_left_table = data
    else:
        stocks_left_table = Stocks.query.filter_by(date=yesterday2).limit(5).all()
        cache.set("data", stocks_left_table)
    us = Global_funds.query.filter_by(date=str(yesterday)).filter_by(header='us').all()
    eu = Global_funds.query.filter_by(date=str(yesterday)).filter_by(header='eu').all()
    asia = Global_funds.query.filter_by(date=str(yesterday)).filter_by(header='asia').all()
    currs = Currency.query.filter_by(date=str(today)).all()

    # stocks_left_table = Stocks.query.filter_by(date=yesterday2).limit(5).all()

    news = News.query.filter_by(date=yesterday).limit(2).all()
    print(stocks_left_table)

    return render_template('main.html', us=us, eu=eu, asia=asia,stocks_left_table=stocks_left_table,subhead=subhead,currs=currs,news=news)


@app.route('/stockinfo/<ticker>')
def stockinfo(ticker):
    top_stock = Stocks.query.filter_by(date=yesterday2).filter_by(symbol=ticker).first()
    stocks_up_container = Stocks.query.filter_by(date=yesterday2).limit(22).all()

    #dk if this will work
    top_stocks = Stocks.query.filter(Stocks.date >= (yesterday - timedelta(days=6)), Stocks.date <= yesterday,
                                     Stocks.symbol == ticker).all()
    days = [stock.date.strftime('%Y-%m-%d') for stock in top_stocks]
    days_list = list(days)
    labels = json.dumps(days_list)

    avg = [float(stock.close) - float(stock.open) for stock in stocks_up_container]



    return  render_template('stockinfo.html', top_stock = top_stock, tickers = stocks_up_container, labels = labels, avg = avg,subhead=subhead )

@app.route('/subscription', methods=['GET', 'POST'])
def subscription():
    if request.method == 'POST':
        email = request.form.get('email')
        if email is None:
            flash('error. enter email')
        else:
            flash('Subscription successful! You will receive daily news updates on stocks.')

    return render_template ('subscription.html')
@app.route('/news')
def news():
    news = News.query.filter_by(date=yesterday).all()
    return render_template('news.html', news=news,subhead=subhead)
@app.route('/news/<id>')
def news_by_id(id):
    news = News.query.filter_by(id=id).first()
    return render_template('news_news.html', news=news,subhead=subhead)


if __name__ == '__main__':
    # scrape_data()
    # with app.app_context():
    #     db.create_all()
    scheduler.start()
    app.run(debug=True)



