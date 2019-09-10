import unittest
from modules.dev_manage.ota_upgrade.ota_upgrade_firmware_history_query import *
from config import readcfg

did_Gary_hub = readcfg.did_Gary_hub
did_Jenny = readcfg.did_Jenny_hub
did_wrong = readcfg.did_wrong


class TestOtaUpgradeFirmwareHistoryQuery(unittest.TestCase):
    """
    查询设备固件升级历史
    """
    def test_ota_upgrade_firmware_history_query_01(self):
        """测试查询设备固件升级历史"""
        result = ota_upgrade_firmware_history_query(did_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_ota_upgrade_firmware_history_query_02(self):
        """测试查询设备固件错误或不存在"""
        result = ota_upgrade_firmware_history_query(did_wrong)
        self.assertIn('"code":706', result.text)

    def test_ota_upgrade_firmware_history_query_03(self):
        """测试查询其他用户的固件升级历史"""
        result = ota_upgrade_firmware_history_query(did_Jenny)
        self.assertIn('"code":706', result.text)

    def test_ota_upgrade_firmware_history_query_05(self):
        """测试查询设备固件为空"""
        result = ota_upgrade_firmware_history_query("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
