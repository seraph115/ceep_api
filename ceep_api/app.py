import logging.config

from flask import Flask, Blueprint
from ceep_api import settings
from ceep_api.api import restplus

from ceep_api.api.endpoints.adbmonitors import ns as adbmonitors_namespace

from ceep_api.api.restplus import api
from ceep_api.database import db


app = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api/1.0')
    api.init_app(blueprint)
    api.add_namespace(adbmonitors_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(settings.FLASK_HOST + ':' + str(settings.FLASK_PORT)))
    app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT, debug=settings.FLASK_DEBUG)
    

if __name__ == "__main__":
    main()
