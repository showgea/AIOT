import unittest
from modules.res_manage.res_query.res_history_aggr_query_new import *
from config import readcfg

subjectId_Gary = readcfg.subjectId_Gary_hub
subjectId_Jenny = readcfg.subjectId_Jenny
attrs = "brightness_level,argb_value"
# 按小时：hour；按天day；按周week；按月month
dimensionType = "hour"
startTime = "1564804800000"
endTime = "1567137600000"
startIndex = 0
size = 100
# max：最大  min：最小   average：平均  frequency：次数  difference：求差
aggrType = "max"


class TestResHistoryAggrQueryNew(unittest.TestCase):
    """
    资源历史聚合结果查询 （返回数据类型全部为String，返回小数点后5位）
    """

    def test_res_history_aggr_query_new_01(self):
        """测试资源历史聚合结果查询"""
        result = res_history_aggr_query_new(subjectId_Gary, attrs, dimensionType, startTime, endTime,
                                            startIndex, size, aggrType)
        self.assertIn('"code":0', result.text)

    def test_res_history_aggr_query_new_02(self):
        """测试查询Id错误或不存在"""
        result = res_history_aggr_query_new(subjectId_Gary.replace("0", "1"), attrs, dimensionType, startTime, endTime,
                                            startIndex, size, aggrType)
        self.assertIn('"code":706', result.text)

    def test_res_history_aggr_query_new_03(self):
        """测试查询其他人的对象id"""
        result = res_history_aggr_query_new(subjectId_Jenny, attrs, dimensionType, startTime, endTime,
                                            startIndex, size, aggrType)
        self.assertIn('"code":706', result.text)

    def test_res_history_aggr_query_new_04(self):
        """测试查询对象id为空"""
        result = res_history_aggr_query_new("", attrs, dimensionType, startTime, endTime,
                                            startIndex, size, aggrType)
        self.assertIn('"code":302', result.text)

    def test_res_history_aggr_query_new_05(self):
        """测试设备资源属性值attr为空"""
        result = res_history_aggr_query_new(subjectId_Gary, "", dimensionType, startTime, endTime,
                                            startIndex, size, aggrType)
        self.assertIn('"code":302', result.text)

    def test_res_history_aggr_query_new_06(self):
        """测试dimensionType为空"""
        result = res_history_aggr_query_new(subjectId_Gary, attrs, "", startTime, endTime,
                                            startIndex, size, aggrType)
        self.assertIn('"code":302', result.text)

    def test_res_history_aggr_query_new_07(self):
        """测试startTime为空"""
        result = res_history_aggr_query_new(subjectId_Gary, attrs, dimensionType, "", endTime,
                                            startIndex, size, aggrType)
        self.assertIn('"code":728', result.text)

    def test_res_history_aggr_query_new_08(self):
        """测试endTime为空"""
        result = res_history_aggr_query_new(subjectId_Gary, attrs, dimensionType, startTime, "",
                                            startIndex, size, aggrType)
        self.assertIn('"code":728', result.text)

    def test_res_history_aggr_query_new_09(self):
        """测试开始时间等于结束时间"""
        result = res_history_aggr_query_new(subjectId_Gary, attrs, dimensionType, startTime, startTime,
                                            startIndex, size, aggrType)
        self.assertIn('"code":0', result.text)

    def test_res_history_aggr_query_new_10(self):
        """测试开始时间大于结束时间"""
        result = res_history_aggr_query_new(subjectId_Gary, attrs, dimensionType, startTime.replace("4", "5"), startTime,
                                            startIndex, size, aggrType)
        self.assertIn('"code":729', result.text)

    def test_res_history_aggr_query_new_11(self):
        """测试startIndex为空"""
        result = res_history_aggr_query_new(subjectId_Gary, attrs, dimensionType, startTime, endTime,
                                            startIndex=None, size=size, aggrType=aggrType)
        self.assertIn('"code":0', result.text)

    def test_res_history_aggr_query_new_12(self):
        """测试size为空"""
        result = res_history_aggr_query_new(subjectId_Gary, attrs, dimensionType, startTime, endTime,
                                            startIndex, size=None, aggrType=aggrType)
        self.assertIn('"code":0', result.text)

    def test_res_history_aggr_query_new_13(self):
        """测试aggrType为空"""
        result = res_history_aggr_query_new(subjectId_Gary, attrs, dimensionType, startTime, endTime,
                                            startIndex, size, aggrType=None)
        self.assertIn('"code":0', result.text)

    def test_res_history_aggr_query_new_14(self):
        """测试size为0"""
        result = res_history_aggr_query_new(subjectId_Gary, attrs, dimensionType, startTime, endTime,
                                            startIndex, size=0, aggrType=aggrType)
        self.assertIn('"code":302', result.text)

    def test_res_history_aggr_query_new_15(self):
        """测试size为1"""
        result = res_history_aggr_query_new(subjectId_Gary, attrs, dimensionType, startTime, endTime,
                                            startIndex, size=1, aggrType=aggrType)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
