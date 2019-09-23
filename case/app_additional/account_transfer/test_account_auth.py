import unittest
from modules.app_additional.account_transfer.account_auth import *


class TestAccountAuth(unittest.TestCase):
    """
   查询家庭项目
    """

    def test_account_auth_01(self):
        """测试查询家庭项目"""
        result = account_auth("123",)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
