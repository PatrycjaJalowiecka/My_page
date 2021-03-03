from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def my_page():
    return render_template("Moja_strona1.html")

@app.route('/kontakt', methods=['GET', 'POST'])
def my_page_kont():
   if request.method == 'GET':
       return render_template("kontakt1.html")
   elif request.method == 'POST':
       print(request.form)
       return redirect("/")