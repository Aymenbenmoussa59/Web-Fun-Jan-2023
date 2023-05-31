from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/<int:x>")
@app.route("/<int:x>/<int:x>")
@app.route("/<int:x>/<color1>")
@app.route("/<int:x>/<int:x>/<color1>")
@app.route("/<int:x>/<int:x>/<color1>/<color2>")

def index(x=8,x=8,color1="red",color2="black"):
    return render_template("index.html", cols=x, rows=x, color1=color1,color2=color2)

if __name__ == "__main__":
    app.run(debug=True)