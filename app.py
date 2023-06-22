from flask import Flask, redirect, url_for, render_template
from models import db, Global_funds
from datetime import date

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

if __name__ == '__main__':
    app.run(debug=True)
