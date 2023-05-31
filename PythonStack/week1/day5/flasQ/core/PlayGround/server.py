from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<int:num>')
def playmulti(num):
    return render_template('index.html', n=num)


@app.route('/play/<int:num>/<color>')
def multi(num, color):
    return render_template('index.html', n=num, c=color)








if __name__=="__main__":
    app.run(debug=True)