from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def my_page():
    return render_template("basic_me.html")

@app.route('/me', methods=['GET'])
def my_page_me():
    return render_template("Moja_strona1.html")