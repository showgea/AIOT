import unittest
from modules.dev_manage.ota_upgrade.ota_query_firmware import *
from config import readcfg

positionId_wrong = readcfg.positionId_wrong
positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
did_Gary_hub = readcfg.did_Gary_hub
did_Jenny = readcfg.did_Jenny_hub
did_wrong = readcfg.did_wrong


class TestOtaQueryFirmware(unittest.TestCase):
    """
    查询可升级的固件
    """
    def test_ota_query_firmware_01(self):
        """测试查询可升级的固件"""
        result = ota_query_firmware(positionId_Gary, did_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_ota_query_firmware_02(self):
        """测试查询位置错误或不存在"""
        result = ota_query_firmware(positionId_wrong, did_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_ota_query_firmware_03(self):
        """测试查询其他用户下可升级的固件"""
        result = ota_query_firmware(positionId_Jenny, did_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_ota_query_firmware_04(self):
        """测试位置为空"""
        result = ota_query_firmware("", did_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_ota_query_firmware_05(self):
        """测试请求参数不传positionId"""
        result = ota_query_firmware(positionId=None, did=did_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_ota_query_firmware_06(self):
        """测试设备id错误或不存在"""
        result = ota_query_firmware(positionId_Gary, did_wrong)
        self.assertIn('"code":706', result.text)

    def test_ota_query_firmware_07(self):
        """测试其他用户下设备id"""
        result = ota_query_firmware(positionId_Gary, did_Jenny)
        self.assertIn('"code":706', result.text)

    def test_ota_query_firmware_08(self):
        """测试设备id为空"""
        result = ota_query_firmware(positionId_Gary, "")
        self.assertIn('"code":0', result.text)

    def test_ota_query_firmware_09(self):
        """测试请求参数不传did"""
        result = ota_query_firmware(positionId_Gary, did=None)
        self.assertIn('"code":0', result.text)

    def test_ota_query_firmware_10(self):
        """测试请求参数不传positionId和did"""
        result = ota_query_firmware(positionId_Gary, did=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
