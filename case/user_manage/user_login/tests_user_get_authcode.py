import unittest
from modules.user_manage.user_login.user_get_authcode import *
from config import readcfg


account_Gary = readcfg.account_Gary
account_mail_Gary = readcfg.account_mail_Gary
countryCode = "+86"
authCodeType = "1"


class TestUserGetAuthCode(unittest.TestCase):
    """获取手机(邮箱)验证码"""

    def test_user_get_authcode_01(self):
        """测试手机获取验证码"""
        result = user_get_authcode(account_Gary, countryCode, authCodeType)
        self.assertIn('"code":0', result.text)

    def test_user_get_authcode_02(self):
        """测试邮箱获取验证码"""
        result = user_get_authcode(account_mail_Gary, countryCode=None, authCodeType=authCodeType)
        self.assertIn('"code":0', result.text)

    def test_user_get_authcode_03(self):
        """测试手机号错误"""
        result = user_get_authcode(account_Gary + "1", countryCode, authCodeType)
        self.assertIn('"code":807', result.text)

    def test_user_get_authcode_04(self):
        """测试获取账号为空"""
        result = user_get_authcode("", countryCode, authCodeType)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
