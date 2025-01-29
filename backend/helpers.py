from flask import jsonify

def response_message(message, status=400):
    return jsonify({"message": message}), status