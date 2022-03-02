from flask import Flask, render_template, url_for, session, redirect, flash
import sqlalchemy
from app.forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm



app = Flask(__name__)

db =SQLAlchemy(app)

@app.route()
def home():
    return("home.html")


@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        form.submit ==  True
        flash(f" Hello", {form.username.data}, "You have been logged in.")
        session["login"]
    else:
        if form.username == "admin@gmail.com" and form.password == "admin":
            flash(f"Hello",{form.username}, " how are you??" )

@app.route("/register")
def register():
    form = RegistrationForm()
    if form.validate_on_submit:
        flash(f"Hey",{form.username} ,"you have been registered.")
        db.session.add()
        db.commit()
    return()
        



if __name__ == "__main__":
    app.run( debug = True)
