from . import TestBaseClass


class AirtimeTest(TestBaseClass):

    def test_send_airtime(self):
        response = self.client.post('/playpen/test/send_airtime')
        self.assertEqual('None', response.json['errorMessage'], msg='Invalid Response,Should be successful')
        self.assertTrue(len(response.json['responses']) > 0, msg='Invalid Response')
