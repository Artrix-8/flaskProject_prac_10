from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<celsius>')
def convert_c_to_f(celsius=""):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"{celsius} Celsius = {fahrenheit} Fahrenheit"


if __name__ == '__main__':
    app.run()
