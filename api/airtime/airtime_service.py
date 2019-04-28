from flask import make_response, jsonify, request, Blueprint
import africastalking

airtime = Blueprint('airtime', __name__, url_prefix="/playpen/test")


@airtime.route('/send_airtime', methods=['POST'])
def send_sms_service():
    req = request.get_json(force=True)
    if {'phoneNo', 'currency', 'amount'} <= set(req):
        airtime_service = africastalking.Airtime
        phone_number = req['phoneNo']
        currency_code = req['currency']
        amount = req['amount']
        response = airtime_service.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
        return make_response(jsonify(response), 200)
    return make_response(jsonify({"error": "Cannot Send Airtime"}), 400)
