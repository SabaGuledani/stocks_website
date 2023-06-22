from flask import Flask,redirect,url_for,render_template
from models import db,Global_funds

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GlobalFunds.sqlite'
db.init_app(app)

with app.app_context():
    db.create_all()



@app.route('/<ticker>')

def home(ticker):


    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
