from flask import Flask, render_template

app = Flask(__name__)


# index route to handle dictionary array.
@app.route('/')
def index():

    isLogged = True
    dict = [{"name":"rajesh", "email":"test@dd.com"}, 
            {"name":"manish", "email":"kota@ko.com"}
           ]
    return render_template('control-flow.html', mydict=dict, isLogged = isLogged)



if __name__ == '__main__':

    app.run()