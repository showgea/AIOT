import unittest
from modules.dev_manage.ota_upgrade.ota_query_firmware_online import *
from config import readcfg

model = "lumi.gateway.aqhm01"
firmwareVersion = "1.4.7_0001"


class TestOtaQueryFirmwareOnline(unittest.TestCase):
    """
    查看线上最新固件
    """
    def test_ota_query_firmware_online_01(self):
        """测试查看线上最新固件"""
        result = ota_query_firmware_online(model, firmwareVersion)
        self.assertIn('"code":0', result.text)

    def test_ota_query_firmware_online_02(self):
        """测试设备类型错误或不存在"""
        result = ota_query_firmware_online(model + "1", firmwareVersion)
        self.assertIn('"code":0', result.text)

    def test_ota_query_firmware_online_03(self):
        """测试固件版本错误或不存在"""
        result = ota_query_firmware_online(model, firmwareVersion + "1")
        self.assertIn('"code":0', result.text)

    def test_ota_query_firmware_online_04(self):
        """测试设备类型为空"""
        result = ota_query_firmware_online("", firmwareVersion)
        self.assertIn('"code":302', result.text)

    def test_ota_query_firmware_online_05(self):
        """测试固件版本为空"""
        result = ota_query_firmware_online(model, "")
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
