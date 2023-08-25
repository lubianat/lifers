from app import app, db
from flask import render_template, redirect, url_for
from app.models import User, Observation


@app.route("/")
def index():
    return render_template("index.html")
