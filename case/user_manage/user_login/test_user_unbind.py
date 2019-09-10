import unittest
from modules.user_manage.user_login.user_unbind import *
from config import readcfg

account_Gary = readcfg.account_Gary
account_mail_Gary = readcfg.account_mail_Gary
authCode = "123456"
countryCode = "+86"


class TestUserUnbind(unittest.TestCase):
    """解绑手机号、邮箱或用户名"""

    def test_user_unbind_01(self):
        """测试解绑手机号"""
        result = user_unbind(account_Gary, authCode, countryCode)
        self.assertIn('"code":820', result.text)

    def test_user_unbind_02(self):
        """测试解绑邮箱"""
        result = user_unbind(account_mail_Gary, authCode)
        self.assertIn('"code":820', result.text)

    def test_user_unbind_03(self):
        """测试验证码不正确"""
        result = user_unbind(account_Gary, authCode + "1")
        self.assertIn('"code":820', result.text)

    def test_user_unbind_04(self):
        """测试解绑用户为空"""
        result = user_unbind("", authCode)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
