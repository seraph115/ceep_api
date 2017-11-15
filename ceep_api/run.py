import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import logging.config

from flask import Flask, Blueprint
from werkzeug.contrib.fixers import ProxyFix

from ceep_api import settings
from ceep_api.api import restplus

from ceep_api.api.endpoints.adbmonitors import ns as adbmonitors_namespace

from ceep_api.api.restplus import api
from ceep_api.database import db


def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    log.debug('Initialize APP...')
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api/1.0')
    api.init_app(blueprint)
    api.add_namespace(adbmonitors_namespace)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)


logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)

app = Flask(__name__)
initialize_app(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

