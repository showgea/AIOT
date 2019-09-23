import unittest
import json
from modules.user_manage.notice_center.user_notice_query_list import *

messageTypes = ["ifttt_app_change", "scene_execute_result", "position_share", "ifttt_execute_result", "alert_execute",
                "dev_online_subdevice"]
# 0未读，1已读（为空查询全部）
state = 0
startTime = readcfg.startTime
endTime = readcfg.endTime
size = readcfg.size
startIndex = readcfg.startIndex


class TestUserNoticeQueryList(unittest.TestCase):
    """
    获取用户的通知消息
    """
    def test_user_notice_query_list_01(self):
        """测试获取用户已读的通知消息（state=1）"""
        result = user_notice_query_list(messageTypes=messageTypes, state=state, startTime=startTime, endTime=endTime,
                                        size=size, startIndex=startIndex)
        length = len(json.loads(result.text)["result"]["resultList"])
        self.assertGreater(length, 1, "查询结果长度：%s" % length)

    def test_user_notice_query_list_02(self):
        """测试请求参数不传startIndex"""
        result = user_notice_query_list(messageTypes=messageTypes, state=state, startTime=startTime, endTime=endTime,
                                        size=size, startIndex=None)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_03(self):
        """测试请求参数不传size"""
        result = user_notice_query_list(messageTypes=messageTypes, state=state, startTime=startTime, endTime=endTime,
                                        size=None, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_04(self):
        """测试请求参数size为0"""
        result = user_notice_query_list(messageTypes=messageTypes, state=state, startTime=startTime, endTime=endTime,
                                        size=0, startIndex=startIndex)
        self.assertIn('"code":302', result.text)

    def test_user_notice_query_list_05(self):
        """测试请求参数size为1"""
        result = user_notice_query_list(messageTypes=messageTypes, state=state, startTime=startTime, endTime=endTime,
                                        size=1, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_06(self):
        """测试请求参数不传endTime"""
        result = user_notice_query_list(messageTypes=messageTypes, state=state, startTime=startTime, endTime=None,
                                        size=size, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_07(self):
        """测试请求参数不传startTime"""
        result = user_notice_query_list(messageTypes=messageTypes, state=state, startTime=None, endTime=endTime,
                                        size=size, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_08(self):
        """测试请求参数startTime大于endTime"""
        result = user_notice_query_list(messageTypes=messageTypes, state=state, startTime=endTime.replace("1", "2"),
                                        endTime=endTime, size=size, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_09(self):
        """测试请求参数startTime等于endTime"""
        result = user_notice_query_list(messageTypes=messageTypes, state=state, startTime=startTime, endTime=startTime,
                                        size=size, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_10(self):
        """测试请求参数state为空（查询用户全部的通知消息）"""
        result = user_notice_query_list(messageTypes=messageTypes, state=None, startTime=startTime, endTime=endTime,
                                        size=size, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_12(self):
        """测试获取用户未读的通知消息（state=0）"""
        result = user_notice_query_list(messageTypes=messageTypes, state=0, startTime=startTime, endTime=None,
                                        size=size, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_13(self):
        """测试请求参数不传messageTypes"""
        result = user_notice_query_list(messageTypes=None, state=0, startTime=startTime, endTime=None, size=size,
                                        startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_14(self):
        """测试请求参数都不穿"""
        result = user_notice_query_list(messageTypes=None, state=None, startTime=None, endTime=None, size=None,
                                        startIndex=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
