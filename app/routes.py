from flask import render_template, url_for, redirect, flash, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
# from app.models import User, Post
from flask_login import login_user, logout_user, current_user,login_required


posts = [
    {
        "author" : "Alec",
        "title" : "First POst",
        "content" : "This is my first post",
        "date_posted" : "10 jan 2022"
    },
    {
        "author" : "Zubair",
        "title" : "Second POst",
        "content" : "This is my Second post",
        "date_posted" : "10 jan 2022"
    }
]





@app.route("/")
def home():
    return render_template("home.html", posts=posts, title='home')


@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        
        flash(f"You have been, {form.username.data},registered", 'success')
        return redirect(url_for("home"))

    return render_template("register.html", form = form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "admin":
            flash(f"You have been, {form.email.data}, Logged in. ", 'success')
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check your email and password.")

    return render_template("login.html", form = form)


@app.route("/post")
def post():

    post = "id"