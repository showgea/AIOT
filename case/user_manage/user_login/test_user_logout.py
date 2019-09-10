import unittest
from modules.user_manage.user_login.user_logout import *


class TestUserLogout(unittest.TestCase):
    """用户退出登录"""

    def test_user_logout_01(self):
        """测试用户退出登录"""
        result = user_logout()
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
