from flask import Blueprint, jsonify, render_template

pagerts = Blueprint("pagerts", __name__)


@pagerts.route("/")
def extreme_start():
    return render_template("index.html")


@pagerts.route("/semone")
def semester_one():
    return jsonify(
        {
            "Error Message": "We're working towards adding the details of this semester to the site."
        }
    )
    # return render_template("semone.html")


@pagerts.route("/semfour")
def semester_four():
    s2sub = [
        {
            "code": "CSET209",
            "title": "Operating Systems - Lectures",
            "link": "/semfour/os",
        },
        {
            "code": "CSET207",
            "title": "Computer Networks - Lectures",
            "link": "/semfour/cn",
        },
        {
            "code": "CSET207-P",
            "title": "Computer Networks - Practicals",
            "link": "/semfour/cnlab",
        },
        {
            "code": "CSET244",
            "title": "Design Analysis of Algorithms - Lectures",
            "link": "/semfour/daa",
        },
        {
            "code": "CSET244-T",
            "title": "Design Analysis of Algorithms - Tutorials",
            "link": "/semfour/daa/tut",
        },
        {
            "code": "CSET228",
            "title": "Data Mining and Predictive Modelling - Lectures",
            "link": "/semfour/dmpm",
        },
        {
            "code": "CSET228-P",
            "title": "Data Mining and Predictive Modelling - Practical",
            "link": "/semfour/dmpm/lab",
        },
        {
            "code": "CSET203",
            "title": "Microcontrollers and Computer Architecture - Assignments",
            "link": "/semfour/mca",
        },
        {"code": "CSET208", "title": "Ethics Final Report", "link": "/semfour/ethics"},
        {"code": "ALL", "title": "Previous Year Questions", "link": "/semfour/pyq"},
    ]

    return render_template("semfour.html", semsub=s2sub)


@pagerts.route("/semtwo")
def semester_two():
    return jsonify(
        {
            "Error Message": "We're working towards adding the details of this semester to the site."
        }
    )
    # return render_template("semtwo.html")


@pagerts.route("/semthree")
def semester_three():
    return jsonify(
        {
            "Error Message": "We're working towards adding the details of this semester to the site."
        }
    )
    # return render_template("semthree.html")
