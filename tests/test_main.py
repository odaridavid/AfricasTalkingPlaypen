from . import TestBaseClass


class MainTest(TestBaseClass):

    def test_endpoint(self):
        response = self.client.get('/')
        self.assertEqual('Success', response.json['SMSMessageData']['Recipients'][0]['status'], msg='Invalid Response')
