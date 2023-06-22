from flask import Flask,redirect,url_for,render_template

import stocks
from models import db,Global_funds



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GlobalFunds.sqlite'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/<ticker>')

def home(ticker):


    return render_template('main.html')


@app.route('/stockinfo')
def stockinfo():
    return render_template('stockinfo.html',
                           previous_close = stocks.previous_close,
                           industry = stocks.industry,
                           stock_open = stocks.stock_open,
                           d_range = stocks.d_range,
                           volume = stocks.volume,
                           after_hours = stocks.after_hours
                           )

#ba
if __name__ == '__main__':
    app.run(debug=True)



