import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        id = int(request.form.get("id")) + 1
        name = request.form.get("name")
        birth_day = request.form.get("birth_day")
        birth_month = request.form.get("birth_month")
        
        db.execute("INSERT INTO birthdays (id, name, month, day) VALUES(?, ?, ?, ?)", id, name, birth_month, birth_day)

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        id = len(birthdays)

        return render_template("index.html", birthdays=birthdays, id=id)


