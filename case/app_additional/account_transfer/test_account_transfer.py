import unittest
from modules.app_additional.account_transfer.account_transfer import *


class TestAccountTransfer(unittest.TestCase):
    """
   项目转移
    """

    def test_account_transfer_01(self):
        """测试项目转移"""
        result = account_transfer("appId", "appId", "appId",)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
