from flask import Flask,render_template
from pymongo import MongoClient

app = Flask(__name__, template_folder='Sweep-Backend')


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.debug = True
    app.run()