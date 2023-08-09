from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('flask-form/template-form.html')



@app.route('/reportpage')
def reportpage():
    lower_latter = False
    upper_letter = False
    num_end = False
    username = request.args.get('username')
    lower_latter =  any(c.islower() for c in username)
    upper_letter =  any(c.isupper() for c in username)
    num_end = username[-1].isdigit()
    alltrueOrNot = lower_latter and upper_letter and num_end
    return render_template('flask-form/reportpage.html', allTrue=alltrueOrNot, 
                           upper_letter= upper_letter, 
                           lower_latter = lower_latter, num_end=num_end)



if __name__ == '__main__':
    app.run(debug=True)