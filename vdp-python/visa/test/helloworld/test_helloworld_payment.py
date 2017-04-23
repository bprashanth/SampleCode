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

class TestCybersourcePayment(unittest.TestCase):

    config = parser.ConfigParser()
    config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'..','configuration.ini'))
    config.read(config_path)

    def setUp(self):
        self.visa_api_client = VisaAPIClient()

    def test_cybersource_payment_authorization(self):
        base_uri = 'vdp/'
        resource_path = 'helloworld'
        query_string = 'apikey=' + self.config.get('VDP','apiKey')
        response = self.visa_api_client.do_x_pay_request(base_uri, resource_path , query_string, '', 'Cybersource Payments Test', 'get')
        self.assertEqual(str(response.status_code) ,"200" ,"Helloworld test failed")
        pass
