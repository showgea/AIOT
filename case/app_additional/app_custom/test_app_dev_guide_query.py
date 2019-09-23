import unittest
from modules.app_additional.app_custom.app_dev_guide_query import *


class TestAppDevSupportQuery(unittest.TestCase):
    """
    查询设备入网信息
    """

    def test_app_dev_guide_query_01(self):
        """测试查询CHN设备入网信息"""
        result = app_dev_guide_query("CHN", "lumi.sensor_switch.aq3")
        self.assertIn('"code":0', result.text)

    def test_app_dev_guide_query_02(self):
        """测试查询USA设备入网信息"""
        result = app_dev_guide_query("USA", "lumi.sensor_switch.aq3")
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
