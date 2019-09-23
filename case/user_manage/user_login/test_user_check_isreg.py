import unittest
from modules.user_manage.user_login.user_check_isreg import *

account_Gary = readcfg.account_Gary
account_mail_Gary = readcfg.account_mail_Gary
account_wrong = readcfg.account_wrong


class TestUserCheckIsreg(unittest.TestCase):
    """检查账户是否已注册"""

    def test_user_check_isreg_01(self):
        """测试检查手机账户是否已注册"""
        result = user_check_isreg(account_Gary)
        isreg = json.loads(result.text)["result"]["isreg"]
        self.assertEqual(1, isreg)

    def test_user_check_isreg_02(self):
        """测试检查邮箱账户是否已注册"""
        result = user_check_isreg(account_mail_Gary)
        isreg = json.loads(result.text)["result"]["isreg"]
        self.assertEqual(1, isreg)

    def test_user_check_isreg_03(self):
        """测试账户错误或不存在"""
        result = user_check_isreg(account_wrong)
        isreg = json.loads(result.text)["result"]["isreg"]
        self.assertEqual(0, isreg)

    def test_user_check_isreg_04(self):
        """测试账户为空"""
        result = user_check_isreg("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
