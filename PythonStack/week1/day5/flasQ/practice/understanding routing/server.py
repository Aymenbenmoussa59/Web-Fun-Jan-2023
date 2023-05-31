from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return f'Hi {name.capitalize()}!'

@app.route('/repeat/<int:num>/<message>')
def repeat_message(num, message):
    repeated_message = message * num
    return repeated_message

if __name__ == '__main__':
    app.run()

