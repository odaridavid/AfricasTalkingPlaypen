from flask import make_response, jsonify, Blueprint
import africastalking

sms = Blueprint('sms', __name__, url_prefix="/playpen/test")


@sms.route('/send_sms', methods=['POST'])
def send_sms_service():
    message_service = africastalking.SMS
    phone_numbers = ["+254717455945"]
    response = message_service.send(message="Test Message", recipients=phone_numbers)
    return make_response(jsonify(response), 200)
