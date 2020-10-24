from flask import jsonify


def handler_response(app, status_code, output, payload = None):
    if not payload:
        payload = {}
    response_object = {
        'response': {
            'Message': output,
            'apiResponse': payload,
            'statusCode': status_code,
        }
    }
    
    response = jsonify(response_object)

    return response
