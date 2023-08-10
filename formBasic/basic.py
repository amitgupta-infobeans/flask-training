from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey123'

class InfoForm(FlaskForm):

    breed = StringField("What Breed are you?")  # attribute
    submit = SubmitField("Submit")

@app.route('/', methods=['GET','POST'])
def index():
    breed = False  # variable
    form = InfoForm()

    if form.validate_on_submit():
        breed = form.breed.data   # to get the form input field name breed
        form.breed.data = ''
    return render_template('index.html', form=form, breed=breed)


if __name__ == '__main__':
    app.run(debug=True)

