from flask import Flask
from flask_cors import CORS

from error_handler import handle_unexpected_error
from routes.generate import generate_router


def create_app():
    app = Flask(__name__)
    CORS(app)

    # ERROR HANDLER
    app.register_error_handler(Exception, handle_unexpected_error)

    # Routers
    app.register_blueprint(generate_router, url_prefix='/generate')

    return app


if __name__ == '__main__':
    create_app().run(host='127.0.0.1', port=8000)
