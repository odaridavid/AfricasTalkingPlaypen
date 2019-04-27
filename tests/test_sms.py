from . import TestBaseClass


class MainTest(TestBaseClass):

    def test_endpoint(self):
        response = self.client.post('/playpen/test/send_sms')
        self.assertEqual('Success', response.json['SMSMessageData']['Recipients'][0]['status'], msg='Invalid Response')
