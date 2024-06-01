from flask import jsonify
from werkzeug.exceptions import HTTPException


# Global error handler for all other exceptions
def handle_unexpected_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), code
