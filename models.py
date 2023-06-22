from datetime import date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Global_funds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    value = db.Column(db.String(40))
    net_change = db.Column(db.String(50))
    percent_change = db.Column(db.String(20))
    month_change = db.Column(db.String(20))
    date = db.Column(db.Date, default=date.today)
    header = db.Column(db.String(20))

class Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10))
    name = db.Column(db.String(60))
    description = db.Column(db.String(150))
    open = db.Column(db.String(20))
    close = db.Column(db.String(20))
    high= db.Column(db.String(20))
    low= db.Column(db.String(20))
    after_hours = db.Column(db.String(20))
    date = db.Column(db.Date, default=date.today)



