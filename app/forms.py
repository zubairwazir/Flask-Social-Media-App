from turtle import title
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min =1, max =15)])
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators= [DataRequired()])
    confirm_password = PasswordField("Confirm Password",validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")

class NewPost(FlaskForm):
    title = StringField("Title", validators =[DataRequired(), Length(min=5, max =22)])
    image = FileField("Image", validators =[FileAllowed(["jpg", "png"])])
    content =TextAreaField("Content", validators =[DataRequired()])
    submit =SubmitField("Submit")

class ContactForm(FlaskForm):
    email = RegistrationForm.email
    name = StringField("Name", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    message = StringField("Message", validators =[DataRequired])
    submit = SubmitField("Send")