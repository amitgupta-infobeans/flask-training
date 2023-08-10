from flask import Flask, render_template, flash, request,session, redirect, url_for
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField

app = Flask(__name__)


app.config['SECRET_KEY'] = "mysecretke1y"

class SimpleForm(FlaskForm):

    breed = StringField("What breed you are?")
    submit = SubmitField('Click me to submit')


@app.route('/', methods =['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():

        session['breed'] = form.breed.data
        flash(f'You have breed : {session["breed"]}')
        return redirect(url_for('index'))

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

    