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

class TestVTSEnroll(unittest.TestCase):

    config = parser.ConfigParser()
    config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'..','configuration.ini'))
    config.read(config_path)
    msg = 'PAN enrollment'
    failure_msg = 'PAN enrollement failed'

    # BLOB field (URL safe base 64 encoded) that represents the encrypted payload for payment
    # instrument. (See Encrypted Payment Instrument).Format: JSON Web Encryption using shared
    # secret made available at time of onboarding.Encrypted Blob of all Payment instrument details.
    # Payment instrument contains: accountNumber, cvv2, last4, name, billingAddress, expirationDate
    request = '''{
      "clientAppID": "98765432",
      "clientWalletAccountID": "FAmwn",
      "consumerEntryMode": "KEYENTERED",
      "encPaymentInstrument": "ew0KICAiYWxnIiA6ICJBMjU2R0NNS1ciLA0KICAiaXYiIDogIm9jV1J1am5MVURkM0RMYjIiLA0KICAidGFnIiA6ICJZTndlajNFLXlkWVBVMHZpUkZGVkNRIiwNCiAgImVuYyIgOiAiQTI1NkdDTSIsDQogICJ0eXAiIDogIkpPU0UiLA0KICAia2lkIiA6ICJJV00xM0Y1NzFOWUNMV0I0QjBVNjExM3A4c2Y5SmVHenI2XzJoYUM5RjltX0FOdExNIiwNCiAgImNoYW5uZWxTZWN1cml0eUNvbnRleHQiIDogbnVsbCwNCiAgImlhdCIgOiBudWxsLA0KICAiY3R5IiA6IG51bGwsDQogICJqdGkiIDogbnVsbA0KfQ.mDaNp3UaTBamM3Os8csqBZHK_TFdJeGcwB7EAm8iFJ0.3p3k8KwdoNVRIXlh.T_Ywtb1a9MeRE1yBUa3PTWZQTerPwRoozz-MB56wCtWZxeqNbUm9chaNUZDrtWOWfaJBVVFl8EwFl4yaIYDfM1XHB5noNYxQTOlh3WbD3wYLyVFpoxtDA3x5sdEIeBnS6SIraIhPQD5a17AkGhj0PRaq2IIfrV9QgcPOY4ktiT0rqLnV0UBJpNIEwmwLIP2bFfn_hwKX1c0WXd2UIVCUlPCxQ88VNfObl91ykSRIBZ1v4G-qIV1oKEWYtinvcZO28gJta86AhTZy3-uTBaoDPXUUKFQz6y-D5CAi72TCfXXVUXl6ELpKpt328BoGPw.G7_Lf3wWgVVi-pj-ZY5-DQ",
      "locale": "en_US",
      "panSource": "MANUALLYENTERED"
    }'''

    def setUp(self):
        self.visa_api_client = VisaAPIClient()
        self.payment_authorization_request = json.loads(self.request)

    def test_vts_enroll(self):
      import pudb; pudb.set_trace()
      base_uri = 'vts/'
      resource_path = 'panEnrollments'
      query_string = 'apikey=' + self.config.get('VDP', 'apiKey')
      respoinse = self.visa_api_client.do_x_pay_request(base_uri, resource_path, query_string, self.payment_authorization_request, self.msg, 'post')
      self.assertEqual(str(respoinse.status_code), "200", self.failure_msg)
      pass
