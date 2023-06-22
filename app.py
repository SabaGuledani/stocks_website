from flask import Flask, redirect, url_for, render_template
from models import db, Global_funds
from datetime import date

#hello aji

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GlobalFunds.sqlite'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    us = Global_funds.query.filter_by(date=str(date.today())).filter_by(header='us').all()
    eu = Global_funds.query.filter_by(date=str(date.today())).filter_by(header='eu').all()
    asia = Global_funds.query.filter_by(date=str(date.today())).filter_by(header='asia').all()

    return render_template('main.html', us=us, eu=eu, asia=asia)



# @app.route('/stockinfo')
# def stockinfo():
#     return render_template('stockinfo.html',
#                            previous_close = stocks.previous_close,
#                            industry = stocks.industry,
#                            stock_open = stocks.stock_open,
#                            d_range = stocks.d_range,
#                            volume = stocks.volume,
#                            after_hours = stocks.after_hours
#                            )

#ba
if __name__ == '__main__':
    app.run(debug=True)



