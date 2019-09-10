import unittest
from modules.service_manage.service_attribute.service_attribute_history_aggr_query import *
from config import readcfg

serviceId = readcfg.serviceId_cube
serviceId_wrong = readcfg.serviceId_wrong
dimensionType = readcfg.dimensionType
startTime = readcfg.startTime
endTime = readcfg.endTime
startIndex = readcfg.startIndex
size = readcfg.size
aggrType = readcfg.aggrType


class TestServiceAttributeHistoryAggrQuery(unittest.TestCase):
    """
    基于service资源历史聚合结果查询
    """

    def test_service_attribute_history_aggr_query_01(self):
        """测试基于service资源历史聚合结果查询"""
        result = service_attribute_history_aggr_query(serviceId, dimensionType, startTime, endTime, startIndex, size,
                                                      aggrType)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_aggr_query_02(self):
        """测试serviceId错误或不存在"""
        result = service_attribute_history_aggr_query(serviceId_wrong, dimensionType, startTime, endTime, startIndex,
                                                      size, aggrType)
        self.assertIn('"code":709', result.text)

    def test_service_attribute_history_aggr_query_03(self):
        """测试serviceId为空"""
        result = service_attribute_history_aggr_query("", dimensionType, startTime, endTime, startIndex, size,
                                                      aggrType)
        self.assertIn('"code":302', result.text)

    def test_service_attribute_history_aggr_query_04(self):
        """测试dimensionType为空"""
        result = service_attribute_history_aggr_query(serviceId, "", startTime, endTime, startIndex, size,
                                                      aggrType)
        self.assertIn('"code":302', result.text)

    def test_service_attribute_history_aggr_query_05(self):
        """测试startTime为空"""
        result = service_attribute_history_aggr_query(serviceId, dimensionType, "", endTime, startIndex, size,
                                                      aggrType)
        self.assertIn('"code":728', result.text)

    def test_service_attribute_history_aggr_query_06(self):
        """测试endTime为空"""
        result = service_attribute_history_aggr_query(serviceId, dimensionType, startTime, "", startIndex, size,
                                                      aggrType)
        self.assertIn('"code":728', result.text)

    def test_service_attribute_history_aggr_query_07(self):
        """测试开始时间等于结束时间"""
        result = service_attribute_history_aggr_query(serviceId, dimensionType, startTime, startTime, startIndex,
                                                      size, aggrType)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_aggr_query_08(self):
        """测试开始时间大于结束时间"""
        result = service_attribute_history_aggr_query(serviceId, dimensionType, endTime, startTime, startIndex,
                                                      size, aggrType)
        self.assertIn('"code":729', result.text)

    def test_service_attribute_history_aggr_query_09(self):
        """测试请求参数不传startIndex"""
        result = service_attribute_history_aggr_query(serviceId, dimensionType, startTime, endTime,
                                                      startIndex=None, size=size, aggrType=aggrType)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_aggr_query_10(self):
        """测试请求参数不传size"""
        result = service_attribute_history_aggr_query(serviceId, dimensionType, startTime, endTime,
                                                      startIndex, size=None, aggrType=aggrType)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_aggr_query_11(self):
        """测试请求参数不传aggrType"""
        result = service_attribute_history_aggr_query(serviceId, dimensionType, startTime, endTime,
                                                      startIndex, size, aggrType=None)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_aggr_query_12(self):
        """测试请求参数不传startIndex、size、aggrType"""
        result = service_attribute_history_aggr_query(serviceId, dimensionType, startTime, endTime,
                                                      startIndex=None, size=None, aggrType=None)
        self.assertIn('"code":0', result.text)

    def test_service_attribute_history_aggr_query_13(self):
        """测试size为0"""
        result = service_attribute_history_aggr_query(serviceId, dimensionType, startTime, endTime, startIndex,
                                                      size=0, aggrType=None)
        self.assertIn('"code":302', result.text)

    def test_service_attribute_history_aggr_query_14(self):
        """测试size为1"""
        result = service_attribute_history_aggr_query(serviceId, dimensionType, startTime, endTime, startIndex,
                                                      size=1, aggrType=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
