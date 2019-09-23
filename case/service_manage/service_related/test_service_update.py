import unittest
from modules.service_manage.service_related.service_update import *

serviceId_on = readcfg.serviceId_on
serviceId_wrong = readcfg.serviceId_wrong
name = "开夜灯"
iconId = readcfg.iconId


class TestServiceUpdate(unittest.TestCase):
    """
    更新service信息（iconId或name）
    """

    def test_service_update_01(self):
        """测试更新service iconId和name"""
        result = service_update(serviceId_on, name, iconId)
        self.assertIn('"code":0', result.text)

    def test_service_update_02(self):
        """测试更新service name"""
        result = service_update(serviceId_on, name, iconId=None)
        self.assertIn('"code":0', result.text)

    def test_service_update_03(self):
        """测试更新service iconId"""
        result = service_update(serviceId_on, name=None, iconId=iconId)
        self.assertIn('"code":0', result.text)

    def test_service_update_04(self):
        """测试更新service的serviceId错误或不存在"""
        result = service_update(serviceId_wrong, name, iconId)
        self.assertIn('"code":709', result.text)

    def test_service_update_06(self):
        """测试更新service的serviceId为空"""
        result = service_update("", name, iconId)
        self.assertIn('"code":302', result.text)

    def test_service_update_07(self):
        """测试更新service不传name和iconId"""
        result = service_update("", name=None, iconId=None)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
