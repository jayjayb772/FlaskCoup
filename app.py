from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mainPage():
    return render_template('mainPage.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()
