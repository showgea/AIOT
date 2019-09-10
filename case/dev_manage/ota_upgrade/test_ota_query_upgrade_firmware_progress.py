import unittest
from modules.dev_manage.ota_upgrade.ota_query_upgrade_firmware_progress import *
from config import readcfg

did_Gary_hub = readcfg.did_Gary_hub
did_Jenny_hub = readcfg.did_Jenny_hub
did_wrong = readcfg.did_wrong


class TestOtaQueryUpgradeFirmwareProgress(unittest.TestCase):
    """
    查询设备当前升级的状态
    """
    def test_ota_query_upgrade_firmware_progress_01(self):
        """测试查询设备当前升级的状态"""
        result = ota_query_upgrade_firmware_progress(did_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_ota_query_upgrade_firmware_progress_02(self):
        """测试设备id错误或不存在"""
        result = ota_query_upgrade_firmware_progress(did_wrong)
        self.assertIn('"code":706', result.text)

    def test_ota_query_upgrade_firmware_progress_03(self):
        """测试查询其他用户下设备当前升级的状态"""
        result = ota_query_upgrade_firmware_progress(did_Jenny_hub)
        self.assertIn('"code":706', result.text)

    def test_ota_query_upgrade_firmware_progress_04(self):
        """测试设备id为空"""
        result = ota_query_upgrade_firmware_progress("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
