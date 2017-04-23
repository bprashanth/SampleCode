from visa.helpers.visa_api_client import VisaAPIClient
import json
import sys
import os
import unittest
if sys.version_info < (3, 0):
    import ConfigParser as parser
else:
    import configparser as parser
'''
@author: visa
'''

class TestCybersourceKeyGeneration(unittest.TestCase):

    config = parser.ConfigParser()
    config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'..','configuration.ini'))
    config.read(config_path)

    def setUp(self):
        self.visa_api_client = VisaAPIClient()
        self.payment_authorization_request = json.loads("{\"encryptionType\": \"RsaOaep256\"}")

    def test_cybersource_key_generation(self):
      import pudb; pudb.set_trace()
      base_uri = 'cybersource/'
      resource_path = 'payments/flex/v1/keys'
      query_string = 'apikey=' + self.config.get('VDP', 'apiKey')
      respoinse = self.visa_api_client.do_x_pay_request(base_uri, resource_path, query_string, self.payment_authorization_request, 'Cybersource Key generation test', 'post')
      self.assertEqual(str(respoinse.status_code), "200", "Cybersource key retrieval test failed")
      pass
