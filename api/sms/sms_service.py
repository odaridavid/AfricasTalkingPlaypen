from flask import make_response, jsonify, Blueprint
import africastalking
import random

sms = Blueprint('sms', __name__, url_prefix="/playpen/test")


@sms.route('/send_sms', methods=['POST'])
def send_sms_service():
    message_service = africastalking.SMS
    ver_code_builder = []
    for x in range(5):
        ver_code_builder.append(random.randint(1, 10))
    separator = ''
    verification_code = separator.join(map(str, ver_code_builder))
    phone_numbers = ["+254717455945"]
    response = message_service.send(message="Verification Code : %s" % verification_code, recipients=phone_numbers)
    return make_response(jsonify(response), 200)
