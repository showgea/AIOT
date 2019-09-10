import unittest
from modules.service_manage.service_attribute.service_attribute_history_query import *
from config import readcfg

serviceId = readcfg.serviceId_cube
serviceId_wrong = readcfg.serviceId_wrong
startTime = readcfg.startTime
endTime = readcfg.endTime
startIndex = readcfg.startIndex
size = readcfg.size


class TestServiceAttributeHistoryQuery(unittest.TestCase):
    """
    基于service资源历史查询
    """

    def test_service_attribute_history_query_01(self):
        """测试基于service资源历史查询"""
        result = service_attribute_history_query(serviceId, startTime, endTime, startIndex, size)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_query_02(self):
        """测试serviceId错误或不存在"""
        result = service_attribute_history_query(serviceId_wrong, startTime, endTime, startIndex, size)
        self.assertIn('"code":709', result.text)

    def test_service_attribute_history_query_03(self):
        """测试serviceId为空"""
        result = service_attribute_history_query("", startTime, endTime, startIndex, size)
        self.assertIn('"code":302', result.text)

    def test_service_attribute_history_query_04(self):
        """测试开始时间等于结束时间"""
        result = service_attribute_history_query(serviceId, startTime, startTime, startIndex, size)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_query_05(self):
        """测试开始时间大于结束时间"""
        result = service_attribute_history_query(serviceId, endTime, startTime, startIndex, size)
        self.assertIn('"code":729', result.text)

    def test_service_attribute_history_query_06(self):
        """测试请求参数不传startTime"""
        result = service_attribute_history_query(serviceId, startTime=None, endTime=endTime, startIndex=startIndex,
                                                 size=size)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_query_07(self):
        """测试请求参数不传endTime"""
        result = service_attribute_history_query(serviceId, startTime, endTime=None, startIndex=startIndex, size=size)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_query_08(self):
        """测试请求参数不传startIndex"""
        result = service_attribute_history_query(serviceId, startTime, endTime, startIndex=None, size=size)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_query_09(self):
        """测试请求参数不传size"""
        result = service_attribute_history_query(serviceId, startTime, endTime, startIndex, size=None)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_query_10(self):
        """测试请求参数不传startTime、endTime、startIndex、size"""
        result = service_attribute_history_query(serviceId, startTime=None, endTime=None, startIndex=None, size=None)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_query_11(self):
        """测试size为0"""
        result = service_attribute_history_query(serviceId, startTime, endTime, startIndex, size=0)
        self.assertIn('"code":302', result.text)

    def test_service_attribute_history_query_12(self):
        """测试size为1"""
        result = service_attribute_history_query(serviceId, startTime, endTime, startIndex, size=1)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
