from flask import Flask, render_template
from ext import app

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/first_aid_info')
def info():
    return render_template("first_aid_info.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

