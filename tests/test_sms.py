from . import TestBaseClass
import json


class SmsTest(TestBaseClass):

    def test_send_sms(self):
        self.number = {
            "phoneNo": "+254717455945"
        }
        response = self.client.post('/playpen/test/send_sms', data=json.dumps(self.number))
        self.assertEqual('Success', response.json['SMSMessageData']['Recipients'][0]['status'], msg='Invalid Response')

    def test_send_sms_no_number(self):
        self.number = {}
        response = self.client.post('/playpen/test/send_sms', data=json.dumps(self.number))
        self.assertEqual('Missing Phone Number to Send Sms', response.json['error'], msg='Invalid Response')
