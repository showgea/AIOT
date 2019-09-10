import unittest
from modules.user_manage.user_login.user_login import *
from config import readcfg

account_Gary = readcfg.account_Gary
password = readcfg.password


class TestUserLogin(unittest.TestCase):
    """用户登录"""

    def test_user_login_01(self):
        """测试正确用户名密码登录"""
        result = user_login(account_Gary, password)
        self.assertIn('"code":0', result.text)

    def test_user_login_02(self):
        """测试用户名错误"""
        result = user_login(account_Gary.replace("2", "1"), password)
        self.assertIn('"code":801', result.text)

    def test_user_login_03(self):
        """测试用户名为空"""
        result = user_login("", password)
        self.assertIn('"code":302', result.text)

    def test_user_login_04(self):
        """测试密码错误"""
        result = user_login(account_Gary, password.replace("2", "1"))
        self.assertIn('"code":810', result.text)

    def test_user_login_05(self):
        """测试密码为空"""
        result = user_login(account_Gary, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
