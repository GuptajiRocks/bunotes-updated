from flask import Flask, jsonify, render_template

from blueprints.dirfunc import pagerts
from blueprints.fullnotes import fnot
from blueprints.semfive import semfi
from blueprints.semfour import semfo
from blueprints.semone import sone
from blueprints.semsix import semsixes
from blueprints.semtwo import stwo

# from models.db import admin

app = Flask(__name__)
app.register_blueprint(pagerts)
app.register_blueprint(sone)
app.register_blueprint(semfo)
app.register_blueprint(stwo)
app.register_blueprint(semfi)
app.register_blueprint(semsixes)
app.register_blueprint(fnot)
# app.register_blueprint(admin)


@app.route("/")
def index_page():
    semesters = [
        {"num": "One", "link": "/semone"},
        {"num": "Two", "link": "/semtwo"},
        {"num": "Three", "link": "/semthree"},
        {"num": "Four", "link": "/semfour"},
        {"num": "Five", "link": "/semfive"},
        {"num": "Six", "link": "/semsix"},
        {"num": "Revision Notes", "link": "/fullnotes"},
    ]

    contrilink = "https://github.com/GuptajiRocks/bunotes-updated"
    return render_template("index.html", semlist=semesters, gitlink=contrilink)


# Goofy Test
@app.route("/index", methods=["GET"])
def myfunc():
    return jsonify({"Name": ["Arihant Gupta", "Vishnu Chityala"]})


@app.route("/details")
def deets():
    return jsonify({"Apps": ["Python", "Flask"], "Deployment": "Vercel"})


if __name__ == "__main__":
    app.run(debug=True)
