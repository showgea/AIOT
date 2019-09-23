import unittest
from modules.app_additional.app_custom.app_position_device_query import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong


class TestAppPositionDeviceQuery(unittest.TestCase):
    """
    查询属于某个位置下的设备信息
    """

    def test_app_position_device_query_01(self):
        """测试查询属于某个位置下的设备信息"""
        result = app_position_device_query(positionId_Gary)
        self.assertIn('"code":0', result.text)

    def test_app_position_device_query_02(self):
        """测试查询其他用户下的位置"""
        result = app_position_device_query(positionId_Jenny)
        self.assertIn('"code":710', result.text)

    def test_app_position_device_query_03(self):
        """测试查询位置错误或不存在"""
        result = app_position_device_query(positionId_wrong)
        self.assertIn('"code":710', result.text)

    def test_app_position_device_query_04(self):
        """测试查询位置为空"""
        result = app_position_device_query("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
