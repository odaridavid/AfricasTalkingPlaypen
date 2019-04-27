from flask import Flask, make_response, jsonify


def create_app():
    app = Flask(__name__)
    app.register_error_handler(500, server_error)
    return app


def server_error(e):
    error_response = {
        "error": "Internal Server Error",
        "status": 500
    }
    return make_response(jsonify(error_response), 500)
