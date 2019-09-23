import unittest
from modules.dev_manage.dev_bind.dev_connect_subdevice_start import *
from config import readcfg

did_Gary = readcfg.did_Gary_hub
did_Jenny = readcfg.did_Jenny_hub
did_wrong = readcfg.did_wrong


class TestDevConnectSubDeviceStart(unittest.TestCase):
    """
    开启子设备入网(APP调用)
    """

    def test_dev_connect_subdevice_start_01(self):
        """测试开启子设备入网(APP调用)"""
        result = dev_connect_subdevice_start(did_Gary, effectTime=None, installCode=None)
        self.assertIn('"code":0', result.text)

    def test_dev_connect_subdevice_start_02(self):
        """测试设备id错误或不存在"""
        result = dev_connect_subdevice_start(did_wrong, effectTime=None, installCode=None)
        self.assertIn('"code":706', result.text)

    def test_dev_connect_subdevice_start_03(self):
        """测试调用其他用户设备入网"""
        result = dev_connect_subdevice_start(did_Jenny, effectTime=None, installCode=None)
        self.assertIn('"code":706', result.text)


if __name__ == '__main__':
    unittest.main()
