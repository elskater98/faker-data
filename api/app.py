from flask import Flask
from flask_cors import CORS

from error_handler import handle_unexpected_error
from routes.time_series import time_series_router
from routes.static import static_router


def create_app():
    app = Flask(__name__)
    CORS(app)

    # ERROR HANDLER
    app.register_error_handler(Exception, handle_unexpected_error)

    # Routers
    app.register_blueprint(time_series_router, url_prefix='/time-series')
    app.register_blueprint(static_router, url_prefix='/static-data')

    return app


if __name__ == '__main__':
    create_app().run(host='127.0.0.1', port=8000)
