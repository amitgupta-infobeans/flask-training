from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():

    value = "this is string value"
    return render_template('basic.html', myName = value)


if __name__ == '__main__':
    app.run()