from flask import Blueprint, render_template

pagerts = Blueprint("pagerts", __name__)


@pagerts.route("/")
def extreme_start():
    return render_template("index.html")


@pagerts.route("/semone")
def semester_one():
    return render_template("semone.html")


@pagerts.route("/semfour")
def semester_four():
    return render_template("semfour.html")


@pagerts.route("/semtwo")
def semester_two():
    return render_template("semtwo.html")


@pagerts.route("/semthree")
def semester_three():
    return render_template("semthree.html")
