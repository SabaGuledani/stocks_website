from flask import Flask, redirect, url_for, render_template
from flask_caching import Cache
from models import db, Global_funds,Stocks
from apscheduler.schedulers.background import BackgroundScheduler
from stocks import get_info
from bloomberg_scrap import get_bloomberg_data
from yahoo_finance import get_popular_stocks
from datetime import date
from datetime import timedelta


today = date.today()
yesterday = today - timedelta(days=1)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GlobalFunds.sqlite'
cache = Cache(app, config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 86400})  # Set cache timeout to 24 hours

def scrape_data():
    main_bloomberg_data = get_bloomberg_data()
    for fund in main_bloomberg_data:
        with app.app_context():
            db.session.add(fund)
            db.session.commit()
            print(f'damatda {fund.name}')

    popular_stocks = get_popular_stocks()
    print(popular_stocks)
    all_stocks_info = get_info(popular_stocks)
    for stock in all_stocks_info:
        with app.app_context():
            db.session.add(stock)
            db.session.commit()
            print(f'damatda {stock.symbol}')



scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(scrape_data, 'cron', hour=6)  # Schedule the scraping task to run at 00:00 (midnight) each day


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
# @cache.cached()
def home():
    # data = cache.get('data')
    # if data:
    #     pass
    # else:
    #     scraped_data = Global_funds.query.filter_by(date=str(date.today())).filter_by(header='us').all()
    #     cache.set("scraped_data", scraped_data)
    us = Global_funds.query.filter_by(date=str(date.today())).filter_by(header='us').all()
    eu = Global_funds.query.filter_by(date=str(date.today())).filter_by(header='eu').all()
    asia = Global_funds.query.filter_by(date=str(date.today())).filter_by(header='asia').all()

    stocks_left_table = Stocks.query.filter_by(date=yesterday).limit(5).all()
    print(stocks_left_table)

    return render_template('main.html', us=us, eu=eu, asia=asia,stocks_left_table=stocks_left_table)


@app.route('/stockinfo/<ticker>')
def stockinfo(ticker):
    top_stock = Stocks.query.filter_by(date=yesterday).filter_by(symbol=ticker).first()
    stocks_up_container = Stocks.query.filter_by(date=yesterday).limit(17).all()

    return  render_template('stockinfo.html', top_stock = top_stock, tickers = stocks_up_container )

@app.route('/subscription')
def subscription():
    pass

if __name__ == '__main__':
    scheduler.start()
    app.run(debug=True)



