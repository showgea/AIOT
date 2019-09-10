import unittest
from modules.user_manage.user_login.user_authcode_login import *
from config import readcfg
from common.get_result_db import get_code

account_Gary = readcfg.account_Gary
account_mail_Gary = readcfg.account_mail_Gary
authCode = "123456"
isClearRedis = "true"


class TestUserAuthCodeLogin(unittest.TestCase):
    """验证码登录"""

    @classmethod
    def setUpClass(cls):
        cls.authCode_phone = get_code()

    def test_user_authcode_login_01(self):
        """测试手机号验证码登录"""
        result = user_authcode_login(account_Gary, self.authCode_phone, isClearRedis)
        self.assertIn('"code":0', result.text)

    def test_user_authcode_login_02(self):
        """测试验证码错误"""
        result = user_authcode_login(account_Gary, authCode, isClearRedis)
        self.assertIn('"code":820', result.text)


if __name__ == '__main__':
    unittest.main()
