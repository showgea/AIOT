import unittest
from modules.positon_manage.position_device_manage.position_device_transfer import *
from config import readcfg

did_Gary_hub = readcfg.did_Gary_hub
positionId_Gary = readcfg.positionId_real1_Gary


class TestPositionDeviceAssign(unittest.TestCase):
    """
    网关设备转移实体顶级位置（跨家分配位置）
    """

    def test_position_device_transfer_01(self):
        """测试网关设备转移实体顶级位置（跨家分配位置）"""
        result = position_device_transfer(did_Gary_hub, positionId_Gary)
        self.assertIn('"code":735', result.text)


if __name__ == '__main__':
    unittest.main()
