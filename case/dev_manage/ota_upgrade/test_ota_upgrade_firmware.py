import unittest
from modules.dev_manage.ota_upgrade.ota_upgrade_firmware import *
from config import readcfg

did_Gary_hub = readcfg.did_Gary_hub
did_Jenny = readcfg.did_Jenny_hub
did_wrong = readcfg.did_wrong


class TestOtaUpgradeFirmware(unittest.TestCase):
    """
    升级固件（一键升级多个固件）
    """
    def test_ota_upgrade_firmware_01(self):
        """测试升级单个固件"""
        result = ota_upgrade_firmware(did_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_ota_upgrade_firmware_02(self):
        """测试升级多个固件"""
        result = ota_upgrade_firmware(did_Gary_hub + "," + did_Jenny)
        self.assertIn('"code":0', result.text)

    def test_ota_upgrade_firmware_03(self):
        """测试升级固件错误或不存在"""
        result = ota_upgrade_firmware(did_wrong)
        self.assertIn('"code":706', result.text)

    def test_ota_upgrade_firmware_04(self):
        """测试升级其他用户的固件"""
        result = ota_upgrade_firmware(did_Jenny)
        self.assertIn('"code":706', result.text)

    def test_ota_upgrade_firmware_05(self):
        """测试升级固件为空"""
        result = ota_upgrade_firmware("")
        self.assertIn('"code":302', result.text)

    def test_ota_upgrade_firmware_06(self):
        """测试升级多个固件中有存错设备id"""
        result = ota_upgrade_firmware(did_Gary_hub + "," + did_wrong)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
