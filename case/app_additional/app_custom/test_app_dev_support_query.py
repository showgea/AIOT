import unittest
from modules.app_additional.app_custom.app_dev_support_query import *


class TestAppDevSupportQuery(unittest.TestCase):
    """
    查询支持的设备列表
    """

    def test_app_dev_support_query_01(self):
        """测试查询CHN支持的设备列表"""
        result = app_dev_support_query("CHN")
        self.assertIn('"code":0', result.text)

    def test_app_dev_support_query_02(self):
        """测试查询USA支持的设备列表"""
        result = app_dev_support_query("USA")
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
