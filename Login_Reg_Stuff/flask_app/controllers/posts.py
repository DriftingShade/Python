from flask_app import app
from flask import flash, render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.post import Post

@app.get("/posts/new")
def new_post():
    return render_template("new_post.html")