import email
import imp
from flask import Flask, flash, redirect, url_for, render_template, request
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_simplelogin import SimpleLogin, is_logged_in
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'something-secret'
app.config['SIMPLELOGIN_USERNAME'] = 'admin'
app.config['SIMPLELOGIN_PASSWORD'] = 'admin'
db = SQLAlchemy(app)
SimpleLogin(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

@app.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add')
def add():
    if is_logged_in():
        return render_template('add.html')
    else:
        return redirect('/')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@app.route('/edit/<int:post_id>')
def edit(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    if is_logged_in():
        return render_template('edit.html', post=post)
    else:
        return redirect('/')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']
    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/deletepost/<int:post_id>', methods=['POST'])
def deletepost(post_id):
    post = Blogpost.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/editpost/<int:post_id>', methods=['POST'])
def editpost(post_id):
    post = Blogpost.query.get_or_404(post_id)

    post.title = request.form['title']
    post.subtitle = request.form['subtitle']
    post.author = request.form['author']
    post.content = request.form['content']

    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
import uuid

app = Flask(__name__)

db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" #relative

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField("Email", validators=[DataRequired(),Email() ])
    password =PasswordField("Password", validators=[DataRequired() ])
    confirm_password =BooleanField("Confirm Password", [DataRequired(), EqualTo("password")])
    submit =SubmitField("Submit")

class LoginForm(FlaskForm):
    email = StringField("Email", validators =[DataRequired(), Email()])
    password = PasswordField("Password", validators =[DataRequired])
    remember = BooleanField("Remember me")
    submit =SubmitField("Login")


class User(db.Model):
    username = db.Column(db.String(20), unique =True, nullable =False)
    email = db.Column(db.String(20), unique =True, nullable = False)
    password = db.Column(db.Integer(10),nullable = False, default ="default.jpg")


@app.route("/")
def contact():
    return ("")


@app.route("")
def home():
    return("<p>Hello.</p>")

@app.route()
def login():
    form = RegistrationForm()
    if form.validate_on_submit:

        flash(f"Hello,{form.email.data}, you have been signed in.")
        return redirect(url_for("home.html", form =form))

@app.route()
def sign_up(form):
    form = LoginForm
    if form.validate_on_submit:
        if form.email.data == "admin@gmail.com" and form.password.data == "admin":
            flash("You have been signed in.")
    return redirect(url_for("login.html"), form = form)

@app.route("POST")
def posts():
    posts = { "content": "post-{}".format(uuid.uuid4().hex),
    "title" : request.form.get("title"),
    "content" : request.form.get("content"),
    "status" : "active"


    }

@app.route(methods =["POST", "GET"])
def add_post():
    if request.method =="GET":
        form.query.fliter_by(post.id)
    return("")

@app.route()
def clock():
    date_time = {"{}/{}/{}".format("time")}
    return()


def clock():
    return()


@app.route(methods = ["POST", "GET"])
def post():
    if request.method == "POST":
        




        return redirect(url_for())


if __name__ == "__main__":
    app.run(debug =True)