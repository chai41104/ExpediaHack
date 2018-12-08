
from flask import Flask
from flask import request

app = Flask(__name__, static_url_path='', static_folder='public')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/query", methods = ['POST'])
def query():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'
