import unittest
import json
from modules.res_manage.res_query.res_history_query import *

subjectId_Gary = readcfg.subjectId_Gary_cube
subjectId_Jenny = readcfg.subjectId_Jenny
subjectId_wrong = readcfg.subjectId_wrong
startTime = readcfg.startTime
endTime = readcfg.endTime
startIndex = readcfg.startIndex
size = readcfg.size
attrs = "device_lqi,pressure_value,temperature_value"


class TestResHistoryQuery(unittest.TestCase):
    """
    资源历史查询
    """

    def test_res_history_query_01(self):
        """测试用户魔方控制器的资源历史查询"""
        result = res_history_query(subjectId_Gary, attrs, startTime, endTime, startIndex, size)
        count = json.loads(result.text)["result"]["count"]
        self.assertGreater(count, 0, "查询魔方上报资源历史查询：%s" % count)

    def test_res_history_query_02(self):
        """测试查询设备Id错误或不存在的当前资源"""
        result = res_history_query(subjectId_wrong, attrs, startTime, endTime, startIndex, size)
        self.assertIn('"code":706', result.text)

    def test_res_history_query_03(self):
        """测试查询其他人的设备id"""
        result = res_history_query(subjectId_Jenny, attrs, startTime, endTime, startIndex, size)
        self.assertIn('"code":706', result.text)

    def test_res_history_query_04(self):
        """测试查询设备id为空"""
        result = res_history_query("", attrs, startTime, endTime, startIndex, size)
        self.assertIn('"code":302', result.text)

    def test_res_history_query_05(self):
        """测试设备资源属性值attr为空"""
        result = res_history_query(subjectId_Gary, "", startTime, endTime, startIndex, size)
        self.assertIn('"code":0', result.text)

    def test_res_history_query_06(self):
        """测试startTime为空"""
        result = res_history_query(subjectId_Gary, attrs, "", endTime, startIndex, size)
        self.assertIn('"code":728', result.text)

    def test_res_history_query_07(self):
        """测试endTime为空"""
        result = res_history_query(subjectId_Gary, attrs, startTime, "", startIndex, size)
        self.assertIn('"code":728', result.text)

    def test_res_history_query_08(self):
        """测试开始时间等于结束时间"""
        result = res_history_query(subjectId_Gary, attrs, startTime, startTime, startIndex, size)
        self.assertIn('"code":0', result.text)

    def test_res_history_query_09(self):
        """测试开始时间大于结束时间"""
        result = res_history_query(subjectId_Gary, attrs, startTime.replace("1", "2"), startTime, startIndex, size)
        self.assertIn('"code":729', result.text)

    def test_res_history_query_10(self):
        """测试请求参数不传startIndex"""
        result = res_history_query(subjectId_Gary, attrs, startTime, endTime, startIndex=None, size=size)
        self.assertIn('"code":0', result.text)

    def test_res_history_query_11(self):
        """测试请求参数不传size"""
        result = res_history_query(subjectId_Gary, attrs, startTime, endTime, startIndex, size=None)
        self.assertIn('"code":0', result.text)

    def test_res_history_query_12(self):
        """测试请求参数不传startIndex、size"""
        result = res_history_query(subjectId_Gary, attrs, startTime, endTime, startIndex=None, size=None)
        self.assertIn('"code":0', result.text)

    def test_res_history_query_13(self):
        """测试size为0"""
        result = res_history_query(subjectId_Gary, attrs, startTime, endTime, startIndex, size=0)
        self.assertIn('"code":302', result.text)

    def test_res_history_query_14(self):
        """测试size为1"""
        result = res_history_query(subjectId_Gary, attrs, startTime, endTime, startIndex, size)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
