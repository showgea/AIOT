import unittest
from modules.user_manage.user_login.user_verify_authcode import *

account_phone = "18682246872"
account_email = "18682246872"
authCode = "123456"
isClearRedis = "1"
countryCode = "+86"
authCodeType = "1"


class TestUserVerifyAuthCode(unittest.TestCase):
    """校验手机(邮箱)验证码"""

    def test_user_verify_authcode_01(self):
        """测试校验手机验证码"""
        result = user_verify_authcode(account_phone, authCode, isClearRedis, countryCode, authCodeType)
        self.assertIn('"code":811', result.text)

    def test_user_verify_authcode_02(self):
        """测试校验邮箱验证码"""
        result = user_verify_authcode(account_email, authCode, isClearRedis, countryCode, authCodeType)
        self.assertIn('"code":811', result.text)


if __name__ == '__main__':
    unittest.main()
