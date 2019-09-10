import unittest
from modules.user_manage.user_login.user_register import *

account = "18682246872"
password = "123456"
authCode = "123456"
nickName = "testRGName"
gender = 0
birthday = "2018-01-01"
area = "shenzhen"


class TestUserRegister(unittest.TestCase):
    """用户注册"""

    def test_user_register_01(self):
        """测试用户注册"""
        result = user_register(account, password, authCode, nickName, gender, birthday, area)
        self.assertIn('"message":"账号已注册"', result.text)


if __name__ == '__main__':
    unittest.main()
