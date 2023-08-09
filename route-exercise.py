from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Go to puppy_name/name and see the result"


@app.route('/puppy_name/<name>')
def puppyLatinfun(name):

    pupname = ''
    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'
    return "<h1> Your puppy name is {}".format(pupname)


if __name__ == '__main__':
    app.run()

