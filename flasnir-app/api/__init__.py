from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Dies ist die Startseite! /users oder /interfaces für mehr Infos.'


from . import data_api

app.register_blueprint(data_api.da)
