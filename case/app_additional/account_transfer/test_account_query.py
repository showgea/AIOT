import unittest
from modules.app_additional.account_transfer.account_query import *


class TestAccountQuery(unittest.TestCase):
    """
   查询家庭项目
    """

    def test_account_query_01(self):
        """测试查询家庭项目"""
        result = account_query("appId", "appId", "appId",)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
