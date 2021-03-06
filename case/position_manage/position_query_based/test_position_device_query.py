import unittest
from modules.positon_manage.position_based_query.position_device_query import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
size = readcfg.size
startIndex = readcfg.startIndex


class TestPositionDeviceQuery(unittest.TestCase):
    """
    查询属于某个位置下的设备信息
    """

    def test_position_device_query_01(self):
        """测试查询用户自己的家下面的位置的设备信息"""
        result = position_device_query(positionId_Gary, size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_device_query_02(self):
        """测试查询位置错误或不存在"""
        result = position_device_query(positionId_wrong, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_position_device_query_03(self):
        """测试查询其他用户下位置"""
        result = position_device_query(positionId_Jenny, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_position_device_query_04(self):
        """测试请求参数size为0"""
        result = position_device_query(positionId_Gary, size=0, startIndex=startIndex)
        self.assertIn('"code":302', result.text)

    def test_position_device_query_05(self):
        """测试请求参数size为1"""
        result = position_device_query(positionId_Gary, size=1, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_device_query_06(self):
        """测试请求参数不传size"""
        result = position_device_query(positionId_Gary, size=None, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_device_query_07(self):
        """测试请求参数不传startIndex"""
        result = position_device_query(positionId_Gary, size, startIndex=None)
        self.assertIn('"code":0', result.text)

    def test_position_device_query_08(self):
        """测试请求参数不传size和startIndex"""
        result = position_device_query(positionId_Gary, size=None, startIndex=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
