import unittest
from modules.user_manage.user_password.user_password_new import *

account_ph = readcfg.account_Gary
account_email = readcfg.account_mail_Gary
password = readcfg.password
authCode = readcfg.authCode_wrong


class TestUserPasswordNew(unittest.TestCase):
    """
    用户设置新密码
    """

    def test_user_password_new_01(self):
        """测试手机用户设置新密码"""
        result = user_password_new(account_ph, password, authCode)
        self.assertIn('"code":0', result.text)

    def test_user_password_new_02(self):
        """测试邮箱用户设置新密码"""
        result = user_password_new(account_email, password, authCode)
        self.assertIn('"code":0', result.text)

    def test_user_password_new_03(self):
        """测试输入手机用户未注册"""
        result = user_password_new(account_ph.replace("2", "3"), password, authCode)
        self.assertIn('message":"账号未注册"', result.text)

    def test_user_password_new_04(self):
        """测试输入邮箱用户未注册"""
        result = user_password_new(account_email.replace("g", "a"), password, authCode)
        self.assertIn('message":"账号未注册"', result.text)

    def test_user_password_reset_04(self):
        """测试输入账号为空"""
        result = user_password_new("", password, authCode)
        self.assertIn('"code":302', result.text)

    def test_user_password_reset_05(self):
        """测试输入密码为空"""
        result = user_password_new(account_ph, "", authCode)
        self.assertIn('"code":302', result.text)

    def test_user_password_reset_06(self):
        """输入验证码为空"""
        result = user_password_new(account_ph, password, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
