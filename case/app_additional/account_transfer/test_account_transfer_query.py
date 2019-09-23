import unittest
from modules.app_additional.account_transfer.account_transfer_query import *


class TestAccountTransferQuery(unittest.TestCase):
    """
   项目转移结果查询
    """

    def test_account_transfer_query_01(self):
        """测试项目转移结果查询"""
        result = account_transfer_query("123",)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
