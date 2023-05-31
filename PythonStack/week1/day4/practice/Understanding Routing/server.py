from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say(name):
    return f"Hi {name.capitalize()}!"

@app.route("/repeat/<int:x>/<word>")
def repeat(x, word):
    return word * x







if __name__ == "__main__":
    app.run(debug=True)
