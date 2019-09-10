import unittest
from modules.user_manage.user_password.user_password_new import *
from common.get_result_db import get_result_from_sql

account_ph = "18682246872"
account_email = "guobing.tang@aqara.com"
# 123456
password = "e10adc3949ba59abbe56e057f20f883e"
authCode = "123456"


class TestUserPasswordNew(unittest.TestCase):
    """
    用户设置新密码
    """

    def test_user_password_new_01(self):
        """手机用户设置新密码"""
        result = user_password_new(account_ph, password, authCode)
        self.assertIn('"code":0', result.text)

    def test_user_password_new_02(self):
        """邮箱用户设置新密码"""
        result = user_password_new(account_email, password, authCode)
        self.assertIn('"code":0', result.text)

    def test_user_password_new_03(self):
        """输入手机用户未注册"""
        result = user_password_new(account_ph.replace("2", "3"), password, authCode)
        self.assertIn('message":"账号未注册"', result.text)

    def test_user_password_new_04(self):
        """输入邮箱用户未注册"""
        result = user_password_new(account_email.replace("g", "a"), password, authCode)
        self.assertIn('message":"账号未注册"', result.text)

    def test_user_password_reset_04(self):
        """输入账号为空"""
        result = user_password_new("", password, authCode)
        self.assertIn('"code":302', result.text)

    def test_user_password_reset_05(self):
        """输入密码为空"""
        result = user_password_new(account_ph, "", authCode)
        self.assertIn('"code":302', result.text)

    def test_user_password_reset_06(self):
        """输入验证码为空"""
        result = user_password_new(account_ph, password, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
