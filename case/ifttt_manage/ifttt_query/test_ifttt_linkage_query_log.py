import unittest
from modules.ifttt_manage.ifttt_query.ifttt_linkage_query_log import *
from config import readcfg

positionId_real1_Gary = readcfg.positionId_real1_Gary
positionId_real1_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
startTime = readcfg.startTime
endTime = readcfg.endTime
size = readcfg.size
startIndex = readcfg.startIndex


class TestIftttLinkageQueryLog(unittest.TestCase):
    """
    查看一系列联动执行的日志
    """

    def test_ifttt_linkage_query_log_01(self):
        """测试查看一系列联动执行的日志"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, startTime, endTime, size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_log_02(self):
        """测试位置id错误或不存在"""
        result = ifttt_linkage_query_log(positionId_wrong, startTime, endTime, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_ifttt_linkage_query_log_03(self):
        """测试其他用户位置联动执行的日志"""
        result = ifttt_linkage_query_log(positionId_real1_Jenny, startTime, endTime, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_ifttt_linkage_query_log_04(self):
        """测试位置id为空"""
        result = ifttt_linkage_query_log("", startTime, endTime, size, startIndex)
        self.assertIn('"code":302', result.text)

    def test_ifttt_linkage_query_log_05(self):
        """测试startTime为空"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, "", endTime, size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_log_07(self):
        """测试endTime为空"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, startTime, "", size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_log_08(self):
        """测试startIndex为空"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, startTime, endTime, size, "")
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_log_09(self):
        """测试size为空"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, startTime, endTime, "", startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_log_10(self):
        """测试开始时间等于结束时间"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, startTime, startTime, size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_log_11(self):
        """测试开始时间大于结束时间"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, endTime, startTime, size, startIndex)
        self.assertIn('"code":729', result.text)

    def test_ifttt_linkage_query_log_12(self):
        """测试size为0"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, startTime, endTime, size=0, startIndex=startIndex)
        self.assertIn('"code":302', result.text)

    def test_ifttt_linkage_query_log_13(self):
        """测试size为1"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, startTime, endTime, size=1, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_log_14(self):
        """测试请求参数不传startTime"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, startTime=None, endTime=endTime, size=size,
                                         startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_log_15(self):
        """测试请求参数不传endTime"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, startTime, endTime=None, size=size,
                                         startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_log_16(self):
        """测试请求参数不传size"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, startTime, endTime, size=None, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_log_17(self):
        """测试请求参数不传startIndex"""
        result = ifttt_linkage_query_log(positionId_real1_Gary, startTime, endTime, size, startIndex=None)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_log_18(self):
        """测试请求参数只传位置id"""
        result = ifttt_linkage_query_log(positionId_real1_Gary)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
