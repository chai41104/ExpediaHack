from service import returnFixDate, returnFlexibleDate
from flask import Flask
from flask import request

app = Flask(__name__, static_url_path='', static_folder='public')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/query", methods = ['POST'])
def query():
    content = request.get_json()
    if content['flexible']:
        return returnFlexibleDate(content)
    else:
        return returnFixDate(content)
        