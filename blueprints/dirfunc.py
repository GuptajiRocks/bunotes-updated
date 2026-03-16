from flask import Blueprint, jsonify, render_template

pagerts = Blueprint("pagerts", __name__)


@pagerts.route("/semone")
def semester_one():
    onename = "One"
    s1sub = [
        {
            "code": "CSET102",
            "title": "Intro to Electrical and Electronics Engineering - Lectures",
            "link": "/semone/cset102/lec",
        },
        {
            "code": "CSET102-T",
            "title": "Intro to Electrical and Electronics Engineering - Tutorials",
            "link": "/semone/cset102/tut",
        },
        {
            "code": "EPHY111L-E",
            "title": "Electromagnetism Lectures",
            "link": "/semtwo/ephy/electro",
        },
        {
            "code": "EPHY111L-M",
            "title": "Mechanics Lectures",
            "link": "/semtwo/ephy/mech",
        },
    ]
    return render_template("seml.html", semsub=s1sub, semname=onename)
    # return jsonify(
    #     {
    #         "Error Message": "We're working towards adding the details of this semester to the site."
    #     }
    # )
    # return render_template("semone.html")


@pagerts.route("/semfour")
def semester_four():
    s4sub = [
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

    fourname = "Four"

    return render_template("seml.html", semsub=s4sub, semname=fourname)


@pagerts.route("/semtwo")
def semester_two():
    twoname = "Two"
    s2sub = [
        {
            "code": "CSET106",
            "title": "Discrete Mathematics - Lectures",
            "link": "/semtwo/dms",
        },
        {
            "code": "CSET106-T",
            "title": "Discrete Mathematics - Tutorials",
            "link": "/semtwo/dms/tut",
        },
        {
            "code": "EMAT102",
            "title": "Linear Algebra - Notes - Dr. Vinay Shukla",
            "link": "/semtwo/emat102/lec",
        },
        {
            "code": "EMAT102-T",
            "title": "Linear Algebra - Tutorials",
            "link": "/semtwo/emat102/tut",
        },
        {
            "code": "CSET109-P",
            "title": "Object Oriented Programming using Java - Practicals",
            "link": "/semtwo/java/lab",
        },
        {
            "code": "EPHY111L-M",
            "title": "Mechanics Lectures",
            "link": "/semtwo/ephy/mech",
        },
        {
            "code": "EPHY111L-E",
            "title": "Electromagnetism Lectures",
            "link": "/semtwo/ephy/electro",
        },
        {
            "code": "CSET102",
            "title": "Intro to Electrical and Electronics Engineering - Lectures",
            "link": "/semone/cset102/lec",
        },
        {
            "code": "CSET102-T",
            "title": "Intro to Electrical and Electronics Engineering - Tutorials",
            "link": "/semone/cset102/tut",
        },
        {
            "code": "CSET105-L",
            "title": "Digital Design - Lectures",
            "link": "/semtwo/dd/lec",
        },
    ]

    return render_template("seml.html", semsub=s2sub, semname=twoname)

    # return jsonify(
    #     {
    #         "Error Message": "We're working towards adding the details of this semester to the site."
    #     }
    # )
    # return render_template("semtwo.html")


@pagerts.route("/semthree")
def semester_three():
    return jsonify(
        {
            "Error Message": "We're working towards adding the details of this semester to the site."
        }
    )
    # return render_template("semthree.html")


@pagerts.route("/semfive")
def semester_five():
    return jsonify(
        {
            "Error Message": "We're working towards adding the details of this semester to the site."
        }
    )


@pagerts.route("/semsix")
def semester_six():
    sixname = "Six"
    s6sub = [
        {
            "code": "noc26-cs10",
            "title": "NPTEL - AI for Management",
            "link": "/semsix/noc26-cs10/assign",
        }
    ]

    return render_template("seml.html", semsub=s6sub, semname=sixname)
