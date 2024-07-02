import os
import secrets

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy.exc import SQLAlchemyError

from database import db
from error_handler import handle_unexpected_error, handle_database_error
from routes.custom import custom_router
from routes.static import static_router
from routes.time_series import time_series_router

API_VERSION = os.getenv('API_VERSION', 'v1')


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', secrets.token_hex(64))

    # SQL ALCHEMY
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Migrate
    migrate = Migrate(app, db)

    CORS(app)

    # ERROR HANDLER
    app.errorhandler(SQLAlchemyError)(handle_database_error)
    app.register_error_handler(Exception, handle_unexpected_error)

    # Routers
    app.register_blueprint(time_series_router, url_prefix=f'api/{API_VERSION}/time-series')
    app.register_blueprint(static_router, url_prefix=f'api/{API_VERSION}/static-data')
    app.register_blueprint(custom_router, url_prefix=f'api/{API_VERSION}/custom-data')

    return app


if __name__ == '__main__':
    create_app().run(host='127.0.0.1', port=8000)
