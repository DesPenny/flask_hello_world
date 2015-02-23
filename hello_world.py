from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World!"
  
@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
  
@app.route("/jedi/<name>/<surname>")
def hello_jedi(name,surname):
    jedi_name =  surname[:3] + name[:2]
    html = """
        <h1>
            Hello {} {}!
        </h1>
        
        <p>
            Your Jedi name is {}!
        </p>
         """
    return html.format(name.title(), surname.title(), jedi_name.title())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)