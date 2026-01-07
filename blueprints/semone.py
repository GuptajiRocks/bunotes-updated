from flask import render_template, Blueprint, jsonify

sone = Blueprint('semone', __name__, url_prefix="/semone")

@sone.route("/one")
def test():
    return jsonify({"Name":"Gooner"})