from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Ismail"}
    posts = [
        {
            "author": {"username": "Sadiyah"},
            "body": "Beautiful day for some MongoDB queries! 👩‍💻",
        },
        {
            "author": {"username": "Tasmiyah"},
            "body": "My Father made me card story to prioritize leaning flask 🤭",
        },
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me={}, password={}".format(
                form.username.data, form.remember_me.data, form.password.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
