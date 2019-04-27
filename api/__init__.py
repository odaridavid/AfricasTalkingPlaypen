from flask import Flask, make_response, jsonify
from .sms.sms_service import sms
import africastalking


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('flask.cfg')
    africastalking.initialize(app.config["AT_USERNAME"], app.config["AT_API_KEY"])
    app.register_error_handler(404, not_found)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(500, server_error)
    app.register_blueprint(sms)
    return app


def server_error(e):
    error_response = {
        "status": str(e)
    }
    return make_response(jsonify(error_response), 500)


def method_not_allowed(e):
    error_response = {
        "status": str(e)
    }
    return make_response(jsonify(error_response), 405)


def not_found(e):
    error_response = {
        "status": str(e)
    }
    return make_response(jsonify(error_response), 404)
