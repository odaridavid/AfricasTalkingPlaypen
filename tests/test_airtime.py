from . import TestBaseClass
import json
from random import SystemRandom


class AirtimeTest(TestBaseClass):

    def test_send_airtime(self):
        cr = SystemRandom()
        amount = str(cr.randrange(start=100, stop=5000, step=50))
        self.airtime = {
            "phoneNo": "+254717455945",
            "currency": "KES",
            "amount": amount
        }
        response = self.client.post('/playpen/test/send_airtime', data=json.dumps(self.airtime))
        self.assertEqual('None', response.json['errorMessage'], msg='Invalid Response,Should be successful')
        self.assertTrue(len(response.json['responses']) > 0, msg='Invalid Response')

    def test_send_airtime_invalid_info(self):
        self.airtime = {}
        response = self.client.post('/playpen/test/send_airtime', data=json.dumps(self.airtime))
        self.assertEqual(response.json['error'], 'Cannot Send Airtime')
