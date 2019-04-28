from flask import make_response, jsonify, Blueprint, request
import africastalking
from random import SystemRandom

sms = Blueprint('sms', __name__, url_prefix="/playpen/test")


@sms.route('/send_sms', methods=['POST'])
def send_sms_service():
    req = request.get_json(force=True)
    if {'phoneNo'} <= set(req):
        phone_numbers = [req['phoneNo']]
        message_service = africastalking.SMS
        ver_code_builder = []
        cryptgen = SystemRandom()
        while len(ver_code_builder) <= 5:
            ver_code_builder.append(cryptgen.randrange(start=0, stop=9))
        separator = ''
        verification_code = separator.join(map(str, ver_code_builder))
        response = message_service.send(message="Verification Code : %s" % verification_code, recipients=phone_numbers)
        return make_response(jsonify(response), 200)
    return make_response(jsonify({"error": "Missing Phone Number to Send Sms"}), 400)
