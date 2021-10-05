from flask import Blueprint
from flask import jsonify

from flasnir.init import *

da = Blueprint("data_api", __name__)


@da.route("/users", methods=["GET"])
def users():
    return jsonify(getusers())


@da.route("/interfaces", methods=["GET"])
def interfaces():
    return jsonify(getinter())
