import unittest
from modules.service_manage.service_subscribe.service_subscribe import *
from config import readcfg

serviceId_on = readcfg.serviceId_on
serviceId_off = readcfg.serviceId_off
serviceId_wrong = readcfg.serviceId_wrong


class TestServiceSubscribe(unittest.TestCase):
    """
    订阅资源
    """
    def test_service_subscribe_01(self):
        """测试订阅资源"""
        result = service_subscribe(serviceId_on)
        self.assertIn('"code":0', result.text)

    def test_service_subscribe_02(self):
        """测试订阅多个资源"""
        result = service_subscribe(serviceId_on + "," + serviceId_off)
        self.assertIn('"code":0', result.text)

    def test_service_subscribe_03(self):
        """测试订阅资源serviceId错误或不存在"""
        result = service_subscribe(serviceId_wrong)
        self.assertIn('"code":709', result.text)

    def test_service_subscribe_04(self):
        """测试订阅多个资源中有serviceId错误或不存在"""
        result = service_subscribe(serviceId_on + "," + serviceId_wrong)
        self.assertIn('"code":0', result.text)

    def test_service_subscribe_05(self):
        """测试订阅资源serviceId为空"""
        result = service_subscribe("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
