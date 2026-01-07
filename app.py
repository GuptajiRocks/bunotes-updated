from flask import Flask, jsonify

from blueprints.dirfunc import pagerts
from blueprints.semone import sone
from blueprints.semfour import semfo

app = Flask(__name__)
app.register_blueprint(pagerts)
app.register_blueprint(sone)
app.register_blueprint(semfo)


# Goofy Test
@app.route("/index", methods=["GET"])
def myfunc():
    return jsonify({"Name": ["Arihant Gupta", "Vishnu Chityala"]})


if __name__ == "__main__":
    app.run(debug=True)
