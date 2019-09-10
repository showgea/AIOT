import unittest
from modules.res_manage.res_query.lock_res_history_query import *
from config import readcfg

subjectId_Gary = readcfg.subjectId_Gary_hub
subjectId_Jenny = readcfg.subjectId_Jenny
attrs = "argb_value"
startTime = "1564804800000"
endTime = "1567137600000"
startIndex = 0
size = 100


class TestLockResHistoryQuery(unittest.TestCase):
    """
    查看门锁的资源历史记录
    """

    def test_lock_res_history_query_01(self):
        """测试查看门锁的资源历史记录"""
        result = lock_res_history_query(subjectId_Gary, attrs, startTime, endTime, startIndex, size)
        self.assertIn('"code":0', result.text)

    def test_lock_res_history_query_02(self):
        """测试查询id错误或不存在"""
        result = lock_res_history_query(subjectId_Gary.replace("0", "1"), attrs, startTime, endTime, startIndex, size)
        self.assertIn('"code":706', result.text)

    def test_lock_res_history_query_03(self):
        """测试查询其他人的id"""
        result = lock_res_history_query(subjectId_Jenny, attrs, startTime, endTime, startIndex, size)
        self.assertIn('"code":706', result.text)

    def test_lock_res_history_query_04(self):
        """测试查询id为空"""
        result = lock_res_history_query("", attrs, startTime, endTime, startIndex, size)
        self.assertIn('"code":302', result.text)

    def test_lock_res_history_query_05(self):
        """测试设备资源属性值attr为空"""
        result = lock_res_history_query(subjectId_Gary, "", startTime, endTime, startIndex, size)
        self.assertIn('"code":0', result.text)

    def test_lock_res_history_query_06(self):
        """测试startTime为空"""
        result = lock_res_history_query(subjectId_Gary, attrs, "", endTime, startIndex, size)
        self.assertIn('"code":728', result.text)

    def test_lock_res_history_query_07(self):
        """测试endTime为空"""
        result = lock_res_history_query(subjectId_Gary, attrs, startTime, "", startIndex, size)
        self.assertIn('"code":728', result.text)

    def test_lock_res_history_query_08(self):
        """测试开始时间等于结束时间"""
        result = lock_res_history_query(subjectId_Gary, attrs, startTime, startTime, startIndex, size)
        self.assertIn('"code":0', result.text)

    def test_lock_res_history_query_09(self):
        """测试开始时间大于结束时间"""
        result = lock_res_history_query(subjectId_Gary, attrs, startTime, startTime.replace("4", "3"), startIndex, size)
        self.assertIn('"code":729', result.text)

    def test_lock_res_history_query_10(self):
        """测试startIndex为空"""
        result = lock_res_history_query(subjectId_Gary, attrs, startTime, endTime, startIndex=None, size=size)
        self.assertIn('"code":0', result.text)

    def test_lock_res_history_query_11(self):
        """测试size为空"""
        result = lock_res_history_query(subjectId_Gary, attrs, startTime, endTime, startIndex, size=None)
        self.assertIn('"code":0', result.text)

    def test_lock_res_history_query_12(self):
        """测试size为0"""
        result = lock_res_history_query(subjectId_Gary, attrs, startTime, endTime, startIndex, size=0)
        self.assertIn('"code":302', result.text)

    def test_lock_res_history_query_13(self):
        """测试size为1"""
        result = lock_res_history_query(subjectId_Gary, attrs, startTime, endTime, startIndex, size)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
