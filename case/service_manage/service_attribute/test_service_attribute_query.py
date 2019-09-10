import unittest
import json
from modules.service_manage.service_attribute.service_attribute_query import *
from config import readcfg

serviceId_on = readcfg.serviceId_on
serviceId_off = readcfg.serviceId_off
serviceId_wrong = readcfg.serviceId_wrong


class TestServiceAttributeQuery(unittest.TestCase):
    """
    读取属性当前值
    """

    def test_service_attribute_query_01(self):
        """测试读取单个属性当前值"""
        result = service_attribute_query(serviceId_on)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_query_02(self):
        """测试读取多个属性当前值"""
        result = service_attribute_query(serviceId_on + "," + serviceId_off)
        length = len(json.loads(result.text)["result"])
        self.assertEqual(2, length)

    def test_service_attribute_query_03(self):
        """测试读取多个属性中有错误或不存在"""
        result = service_attribute_query(serviceId_on + "," + serviceId_wrong)
        length = len(json.loads(result.text)["result"])
        self.assertEqual(1, length)

    def test_service_attribute_query_04(self):
        """测试读取单个属性id错误或不存在"""
        result = service_attribute_query(serviceId_wrong)
        self.assertIn('"code":709', result.text)

    def test_service_attribute_query_05(self):
        """测试读取属性id为空"""
        result = service_attribute_query("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
