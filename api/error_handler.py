from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import HTTPException

from database import db


# Global error handler for all other exceptions
def handle_unexpected_error(e: Exception):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), code


def handle_database_error(error: SQLAlchemyError):
    db.session.rollback()
    return jsonify({'error': 'Database operation failed', 'details': str(error)}), 500
