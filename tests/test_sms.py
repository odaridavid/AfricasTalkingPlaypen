from . import TestBaseClass


class SmsTest(TestBaseClass):

    def test_send_sms(self):
        response = self.client.post('/playpen/test/send_sms')
        self.assertEqual('Success', response.json['SMSMessageData']['Recipients'][0]['status'], msg='Invalid Response')
