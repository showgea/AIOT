import unittest
from modules.service_manage.service_subscribe.service_unsubscribe import *

serviceId_on = readcfg.serviceId_on
serviceId_off = readcfg.serviceId_off
serviceId_wrong = readcfg.serviceId_wrong


class TestServiceSubscribe(unittest.TestCase):
    """
    取消资源订阅
    """
    def test_service_unsubscribe_01(self):
        """测试取消资源订阅"""
        result = service_unsubscribe(serviceId_on)
        self.assertIn('"code":0', result.text)

    def test_service_unsubscribe_02(self):
        """测试取消订阅多个资源"""
        result = service_unsubscribe(serviceId_on + "," + serviceId_off)
        self.assertIn('"code":0', result.text)

    def test_service_unsubscribe_03(self):
        """测试取消订阅资源serviceId错误或不存在"""
        result = service_unsubscribe(serviceId_wrong)
        self.assertIn('"code":709', result.text)

    def test_service_unsubscribe_04(self):
        """测试取消订阅多个资源中有serviceId错误或不存在"""
        result = service_unsubscribe(serviceId_on + "," + serviceId_wrong)
        self.assertIn('"code":0', result.text)

    def test_service_unsubscribe_05(self):
        """测试取消订阅资源serviceId为空"""
        result = service_unsubscribe("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
