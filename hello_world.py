import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('template.html', my_string="Hello World!")
  
@app.route("/hello/<name>")
def hello_person(name):
    return render_template('template.html', my_string="Hello " + name)
  
@app.route("/jedi/<name>/<surname>")
def hello_jedi(name,surname):
    jedi_name =  surname[:3] + name[:2]
    return render_template('template.html', my_string= "Your Jedi name is " + jedi_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)