from flask import make_response, jsonify, Blueprint
import africastalking

airtime = Blueprint('airtime', __name__, url_prefix="/playpen/test")


@airtime.route('/send_airtime', methods=['POST'])
def send_sms_service():
    airtime_service = africastalking.Airtime
    # Static Values
    phone_number = "+254717455945"
    currency_code = "KES"
    amount = "100"
    response = airtime_service.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
    return make_response(jsonify(response), 200)
