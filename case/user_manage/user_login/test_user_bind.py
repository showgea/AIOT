import unittest
import json
from modules.user_manage.user_login.user_bind import *

account_phone = "18682246872"
account_email = "guobing.tang@aqara.com"
authCode = "123456"
countryCode = "+86"


class TestUserBind(unittest.TestCase):
    """绑定手机号、邮箱或用户名"""

    def test_user_bind_01(self):
        """测试绑定手机号"""
        result = user_bind(account_phone, authCode, countryCode)
        self.assertIn('"code":820', result.text)

    def test_user_bind_02(self):
        """测试绑定邮箱"""
        result = user_bind(account_email, authCode)
        self.assertIn('"code":820', result.text)

    def test_user_bind_03(self):
        """测试验证码不正确"""
        result = user_bind(account_phone, authCode + "1")
        self.assertIn('"code":820', result.text)

    def test_user_bind_04(self):
        """测试绑定用户为空"""
        result = user_bind("", authCode)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
