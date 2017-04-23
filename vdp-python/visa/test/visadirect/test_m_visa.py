from visa.helpers.visa_api_client import VisaAPIClient
import json
import sys
import os
import datetime
import unittest
if sys.version_info < (3, 0):
    import ConfigParser as parser
else:
    import configparser as parser
'''
@author: visa
'''

class TestMVisa(unittest.TestCase):

    config = parser.ConfigParser()
    config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'..','configuration.ini'))
    config.read(config_path)

    def setUp(self):
        date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        self.visa_api_client = VisaAPIClient()
        self.m_visa_transaction_request = json.loads('''{
            "acquirerCountryCode": "643",
            "acquiringBin": "400171",
            "amount": "124.05",
            "businessApplicationId": "CI",
            "cardAcceptor": {
              "address": {
                "city": "Bangalore",
                "country": "IND"
              },
            "idCode": "ID-Code123",
            "name": "Card Accpector ABC"
            },
            "localTransactionDateTime": "'''+ date +'''",
            "merchantCategoryCode": "4829",
            "recipientPrimaryAccountNumber": "4123640062698797",
            "retrievalReferenceNumber": "430000367618",
            "senderAccountNumber": "4541237895236",
            "senderName": "Mohammed Qasim",
            "senderReference": "1234",
            "systemsTraceAuditNumber": "313042",
            "transactionCurrencyCode": "USD",
            "transactionIdentifier": "381228649430015"
        }''')

    def test_mVisa_transactions(self):
        # import pudb; pudb.set_trace()
        base_uri = 'visadirect/'
        resource_path = 'mvisa/v1/cashinpushpayments'
        response = self.visa_api_client.do_mutual_auth_request(base_uri + resource_path, self.m_visa_transaction_request, 'M Visa Transaction Test','post')
        # query_string = 'apikey=' + self.config.get('VDP', 'apiKey')
        # response = self.visa_api_client.do_x_pay_request(base_uri, resource_path, query_string, self.m_visa_transaction_request, 'M Visa Transaction Test', 'post');
        self.assertEqual(str(response.status_code) ,"200" ,"M Visa Transaction test failed")
        pass
