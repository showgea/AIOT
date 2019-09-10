import unittest
from modules.positon_manage.position_device_manage.position_device_assign import *
from config import readcfg

dids = "lumi.158d00026e9e32"
dids_Jenny = "virtual.38136362841914"
positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
layout = "1"


class TestPositionDeviceAssign(unittest.TestCase):
    """
    为设备分配位置
    """

    def test_position_device_assign_01(self):
        """测试为设备分配位置"""
        result = position_device_assign(dids, positionId_Gary, layout)
        self.assertIn('"code":0', result.text)

    def test_position_device_assign_02(self):
        """测试分配位置错误或不存在"""
        result = position_device_assign(dids, positionId_Gary.replace("5", "6"), layout)
        self.assertIn('"code":710', result.text)

    def test_position_device_assign_03(self):
        """测试分配设备错误不存在"""
        result = position_device_assign(dids.replace("1", "2"), positionId_Gary, layout)
        self.assertIn('"code":706', result.text)

    def test_position_device_assign_04(self):
        """测试分配设备为空"""
        result = position_device_assign("", positionId_Gary, layout)
        self.assertIn('"code":302', result.text)

    def test_position_device_assign_05(self):
        """测试分配位置为空"""
        result = position_device_assign(dids, "", layout)
        self.assertIn('"code":302', result.text)

    def test_position_device_assign_06(self):
        """测试分配自己的设备到其他人位置下"""
        result = position_device_assign(dids, positionId_Jenny, layout)
        self.assertIn('"code":710', result.text)

    def test_position_device_assign_07(self):
        """测试分配其他人的设备到自己位置下"""
        result = position_device_assign(dids_Jenny, positionId_Gary, layout)
        self.assertIn('"code":706', result.text)


if __name__ == '__main__':
    unittest.main()
