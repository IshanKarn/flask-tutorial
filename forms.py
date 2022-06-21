from flask_wtf import Form
from wtforms import Form, StringField, RadioField, TextAreaField, IntegerField, SelectField, SubmitField

from wtforms import validators, ValidationError

class ContactForm1(Form):
    name = StringField("Name of student")
    submit = SubmitField("Send")

class ContactForm(Form):
    name = StringField("Student Name", [validators.DataRequired("Please enter your name.")])
    gender = RadioField('Gender', choices=[('M','Male'), ('F','Female')])
    address = TextAreaField("Address")
    email = StringField('Email', [validators.DataRequired("Please enter your email address."), validators.Email('Please enter a valid email address.')])
    age = IntegerField('Age')
    languages = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'Python'), ('js', 'Javascript')])
    submit = SubmitField('Send')