from flask import jsonify, current_app


# TODO: errorhandler 404


class ValidationError(Exception):
    def __init__(self, error):
        self.dict = error


def bad_request(error):
    response = jsonify({'status': 400, 'error': error})
    response.status_code = 400
    return response


# @current_app.errorhandler(ValidationError)
# def validation_error(e):
#     return bad_request(e.dict)
