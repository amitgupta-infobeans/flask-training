from flask import Flask

app = Flask(__name__)


@app.route('/')  # 127.0.0.1:5000
def index():
    return '<h1>Hello World</h2>'


@app.route('/information')   #127.0.0.1:5000/information
def information():
    return '<h1>Information Page...</h1>'

@app.route('/userprofile/<name>')
def userprofile(name):
    return ("<h1>This is route Example with two {}.</h1>".format(s))



if __name__ == '__main__':
    #app.run(debug=True)  #debug = True
    app.run()
    