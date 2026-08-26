from flask import Blueprint, redirect, render_template

fnot = Blueprint("fnot", __name__, url_prefix="/fullnotes")

backlink = "/fullnotes"
ssnames = "N"
