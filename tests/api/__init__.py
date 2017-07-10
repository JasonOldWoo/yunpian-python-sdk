'''
Created on Jul 4, 2017

@author: dzh
'''

import unittest

from sdk.model.constant import *
from sdk.ypclient import YunpianClient


class TestYunpianApi(unittest.TestCase):

    APIKEY = '2daab1114c69c9c41d1172b0ad8c392d'

    CONF = {YP_FLOW_HOST:'https://test-api.yunpian.com', YP_SIGN_HOST:'https://test-api.yunpian.com', \
            YP_SMS_HOST:'https://test-api.yunpian.com', YP_TPL_HOST:'https://test-api.yunpian.com', \
            YP_USER_HOST:'https://test-api.yunpian.com', YP_VOICE_HOST:'https://test-api.yunpian.com'}

    def setUp(self):
        self.clnt = YunpianClient(TestYunpianApi.APIKEY, TestYunpianApi.CONF)
        pass


    def tearDown(self):
        pass

    def toJson(self, obj):
        import json
        return json.dumps(obj.__dict__)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
