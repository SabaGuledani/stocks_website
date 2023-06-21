from flask import Flask,redirect,url_for,render_template


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your-database-uri'
db.init_app(app)


@app.route('/')
def home():

    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
