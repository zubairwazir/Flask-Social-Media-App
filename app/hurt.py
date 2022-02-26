from enum import unique
import profile
from unittest import result
# from logging import _Level
from flask import Flask, url_for, render_template, redirect, flash, request, session
from flask_socketio import SocketIO, send
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_login import login_user, logout_user
from pusher import Pusher

from app.forms import LoginForm, NewPost, RegistrationForm


app =Flask(__name__)

db = SQLAlchemy(app)
socketio = SocketIO(app)

mail = Mail(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"


class Post(db.Model):
    title= db.Column(db.String(Length(min=3, max = 35)))
    content = db.Column(db.String(Length(min=20, max=5000)))
    post_image = db.Column(db.String(20))


class Profile(db.Model):
    name = db.Column(db.String(20), nullable =False)
    nickname = db.Column(db.String(20))



class ProfileFootball(db.Model):
    name =db.Column(db.String(Length(min=5, max=18), unique =True), nullable = False)
    running_speed = db.Column(db.String(min=1, max=2))
    passing_ability =db.Column(db.String(min=4, max=20))
    level_status =db.Column(db.String(min=5, max=12))
    age = db.Column(db.Integer(min=2, max=2), nullable = False)
    race = db.Column(db.String(min=3, max =12), nullable = False)
    height = db.Column(db.String(min=2, max=2), nullable = False)
    weight =db.Column(db.Integer(min=2, max=3))


class ProfileBasketball(db.Model):
    name = db.Column(db.String(Length(min=5, max = 18), unique = True), nullable = False)
    running_speed = db.Column(db.String(min=1, max=2))
    level_status = db.Column(db.String(min=5, max =12))
    age = db.Column(db.Integer(min=2, max=2), nullable = False)
    race = db.Column(db.String(min=3, max =12), nullable = False)
    height = db.Column(db.String(min=2, max=2), nullable = False)
    weight =db.Column(db.Integer(min=2, max=3))




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    sport = db.Column(db.String(20), backref ="sport")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class RunningSpeed(db.Model):
    status = db.Column(db.String(10), nullable = False)
    running_speed = db.Column(db.Integer(3), nullable = False)
    strength = db.Column(db.Integer(4), nullable = False)



app.route("/runningback")
def running_back():

    return("rb.html")


app.route("/quarterback")
def quarter_back():
    qb = ProfileFootball
    ques_of_qb = flash("Are you a quarter_back","Y/N")
    if ques_of_qb == "Y":
        qb.passing_ability == True
        flash(f"You will be scouted for the {stat_qb}")
        return("qb.html")
    else:
        return("")

@app.route("/defensiveline")
def defensive_line():
    return("dl.html")



@app.route("/offensiveline")
def offensive_line():
    return("of.html")

@app.route("/widereceiver")
def wide_receiver():
    return("wr.html")


@app.route("/kicker")
def kicker():
    
    return("kicker.html")


@app.route("/")
def home():
    
    return render_template("home.html")


@app.route("/addpost")
def add_post():
    post = Post()
    make_post ={
        'id': "post-{}".format(uuid.uuid4().hex),
        "Author": request.form.get("author"),
        "title" : request.form.get("title"),
        "content": request.form.get("content"),
        "image": request.form.get("post_image")
        }
    if post == True:
        if post.post_image.data and post.title.data and post.content.data:
            make_post = True             
            relationship = Post(title =post.title.data, content =post.content.data, post_image = post.post_image.data )
        db.session.add(relationship)
        db.session.commit
        flash("Your post has been created.")
    return redirect(url_for("home.html", make_post = make_post))


@app.route("/updatepost", methods = ["PUT", "DELETE"])
def delete_post():
    post = Post()
    post.query.get_or_404(post_id)
    data = {"id":"post-{}".format(uuid.uuid4()).hex}
    if request.method == "DELETE":
        data["post"]= "deleted"
        pusher.trigger("post", "deleted", data, post = post)


@app.route('/editpost/<int:post_id>', methods=['POST'])
def editpost(post_id):
    post = Post.query.get_or_404(post_id)

    post.title = request.form['title']
    post.content = request.form['content']
    post.author = request.form['author']
    post.content = request.form['content']

    db.session.commit()
    return redirect('/')

@app.route("/register")
def register():
    form = RegistrationForm()
    if form.validate_on_submit:
        flash(f"Hello, {form.username.data}", "thank you for registering.")
        return redirect(url_for("hurt.html"))

@app.route("/login", methods =["GET", "POST"])
def login(form):
    if request.method == "POST" and form.validate_on_submit() :
        request.form.get("username")
        request.form.get("password")
        flash(f"Hello, {form.username.data} You have been logged in.")
        return redirect(url_for("home.html"))



@app.route("/logout")
def logout():
    user =User()
    if logout== True:
        session.pop(f"{user}")
        logout_user("logout_user")
    return redirect(url_for("login.html"))

app.route("/Contact")
def contact():
    form = LoginForm()
    msg = Message(",Hello, how are you?", sender ="{{form.email}}" )
    if form.connect():
        for user in form.username:
            if LoginForm.submit == "POST":
                msg.send 
    return redirect (url_for("contact"), form = form)

@socketio.on("message")
def message(msg):
    print("message"+ msg)
    send(msg, broadcast = True)


if __name__ =="__main__":
    socketio.run(app)
    app.run(debug =True)