from flask import Flask, jsonify

from blueprints.dirfunc import pagerts
from blueprints.semfour import semfo
from blueprints.semone import sone
from blueprints.semtwo import stwo

# from models.db import admin

app = Flask(__name__)
app.register_blueprint(pagerts)
app.register_blueprint(sone)
app.register_blueprint(semfo)
app.register_blueprint(stwo)
# app.register_blueprint(admin)


# Goofy Test
@app.route("/index", methods=["GET"])
def myfunc():
    return jsonify({"Name": ["Arihant Gupta", "Vishnu Chityala"]})


@app.route("/details")
def deets():
    return jsonify({"Apps": ["Python", "Flask"], "Deployment": "Vercel"})


if __name__ == "__main__":
    app.run(debug=True)
