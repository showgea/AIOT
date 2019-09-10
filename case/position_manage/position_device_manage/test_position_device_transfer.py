import unittest
from modules.positon_manage.position_device_manage.position_device_transfer import *
from config import readcfg

deviceId = "lumi.158d0003930b2a"
positionId_Gary = readcfg.positionId_real1_Gary


class TestPositionDeviceAssign(unittest.TestCase):
    """
    网关设备转移实体顶级位置（跨家分配位置）
    """

    def test_position_device_transfer_01(self):
        """测试网关设备转移实体顶级位置（跨家分配位置）"""
        result = position_device_transfer(deviceId, positionId_Gary)
        self.assertIn('"code":735', result.text)


if __name__ == '__main__':
    unittest.main()
