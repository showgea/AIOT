import unittest
from modules.user_manage.user_info.user_query_info_byauthcode import *
from common.get_result_db import get_common_code
from config import readcfg

account_mail_Gary = readcfg.account_mail_Gary
authCode = "123456"


class TestUserQueryInfoByAuthCode(unittest.TestCase):
    """
    根据验证码及账号获取用户基本信息
    """
    @classmethod
    def setUpClass(cls):
        cls.authCode_email = get_common_code()

    def test_user_query_info_byauthcode_01(self):
        """测试根据验证码及账号获取用户基本信息"""
        result = user_query_info_byauthcode(account_mail_Gary, self.authCode_email)
        # print(self.authCode_phone)
        self.assertIn('"code":0', result.text)

    def test_user_query_info_byauthcode_02(self):
        """测试账号错误或不存在"""
        result = user_query_info_byauthcode(account_mail_Gary.replace("n", "a"), authCode)
        self.assertIn('"code":811', result.text)

    def test_user_query_info_byauthcode_03(self):
        """测试账号为空"""
        result = user_query_info_byauthcode("", authCode)
        self.assertIn('"code":302', result.text)

    def test_user_query_info_byauthcode_04(self):
        """测试验证码为空"""
        result = user_query_info_byauthcode(account_mail_Gary, "")
        self.assertIn('"code":302', result.text)

    def test_user_query_info_byauthcode_05(self):
        """测试验证码错误"""
        result = user_query_info_byauthcode(account_mail_Gary, authCode)
        self.assertIn('"code":811', result.text)


if __name__ == '__main__':
    unittest.main()
