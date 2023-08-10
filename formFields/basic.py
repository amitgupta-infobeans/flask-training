from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField,
                     RadioField, SelectField, TextAreaField)


from wtforms.validators import DataRequired 


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey123'

class InfoForm(FlaskForm):

    breed        = StringField("What Breed are you?", validators=[DataRequired()])  #attribute
    neutered     = BooleanField('Have you been neutered?')
    mood         = RadioField("Please choose your mood:",choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food_choice  = SelectField(u'pick your favorite food:', choices=[('chi', 'Chicken'),('bf', 'beef'), ('fist', 'Fish')  ])
    feedback     = TextAreaField()
    submit       = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
   
    form = InfoForm()

    if form.validate_on_submit():
        breed = form.breed.data   
        session['breed']    = form.breed.data # to get the form input field name
        session['neutered'] = form.neutered.data
        session['mood']     = form.mood.data
        session['food_choice']     = form.food_choice.data
        session['feedback'] = form.feedback.data
        return redirect (url_for('thankyou'))
    
    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)

