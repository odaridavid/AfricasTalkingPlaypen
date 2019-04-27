from flask import make_response, jsonify
from api import create_app
import africastalking
import os

app = create_app()


@app.route('/send_sms')
def at_sms_service():
    africastalking.initialize(os.getenv("AT_USERNAME"), os.getenv("AT_API_KEY"))
    sms = africastalking.SMS
    response = sms.send("Test Message", ["+254717455945"])
    return make_response(jsonify(response), 200)


if __name__ == '__main__':
    app.run()
