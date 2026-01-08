from flask import Blueprint, jsonify, render_template

stwo = Blueprint("stwo", __name__, url_prefix="/semtwo")


@stwo.route("/java")
def test():
    return jsonify({"Name": "Gooner"})
