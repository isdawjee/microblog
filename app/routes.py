from flask import render_template

from app import app


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
