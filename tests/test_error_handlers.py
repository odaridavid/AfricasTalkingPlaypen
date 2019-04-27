from . import TestBaseClass


class ErrorHandlersTest(TestBaseClass):

    def test_endpoint_not_found(self):
        response = self.client.post('/playpen/test/send_sm')
        self.assertIn('404 Not Found', response.json['status'],
                      msg='Invalid Response,Resource Should be Non Existent')

    def test_endpoint_access_with_invalid_method(self):
        response = self.client.get('/playpen/test/send_sms')
        self.assertIn('405 Method Not Allowed', response.json['status'],
                      msg='Invalid Response,Should Not Have Access')
