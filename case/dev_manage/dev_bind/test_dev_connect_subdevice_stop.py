import unittest
from modules.dev_manage.dev_bind.dev_connect_subdevice_stop import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
did_Gary = readcfg.did_Gary_hub
did_Jenny = readcfg.did_Jenny_hub


class TestDevConnectSubDeviceStop(unittest.TestCase):
    """
    关闭子设备入网(APP调用)
    """

    def test_dev_connect_subdevice_stop_01(self):
        """测试关闭子设备入网(APP调用)"""
        result = dev_connect_subdevice_stop(did_Gary)
        self.assertIn('"code":0', result.text)

    def test_dev_connect_subdevice_stop_02(self):
        """测试设备id错误或不存在"""
        result = dev_connect_subdevice_stop(did_Gary.replace("1", "2"))
        self.assertIn('"code":706', result.text)

    def test_dev_connect_subdevice_stop_03(self):
        """测试关闭其他用户设备"""
        result = dev_connect_subdevice_stop(did_Jenny)
        self.assertIn('"code":706', result.text)


if __name__ == '__main__':
    unittest.main()
