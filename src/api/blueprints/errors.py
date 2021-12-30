from http import HTTPStatus
from flask import Blueprint, json
from marshmallow.exceptions import ValidationError

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(Exception)
def handle_unexpected_error(error):
    status_code = 500
    response = {
        'error': {
            'type': 'UnexpectedException',
            'message': 'An unexpected error has occurred.'
        }
    }

    return json.dumps(response), status_code

@errors.app_errorhandler(ValidationError)
def handle_unexpected_error(error):
    status_code = 400
    response = {
        'error': {
            'type': 'Bad Request',
            'message': error.messages
        }
    }

    return json.dumps(response), status_code