import unittest
import json
from modules.family_share.share_message_query import *

size = "100"
start_index = 0
start_time = "1564632000000"
end_time = "1567137600000"
state = ["07"]


class TestMessageQuery(unittest.TestCase):
    """
    分享日志查询
    """

    def test_share_message_query_01(self):
        """测试查询2019/8/12 12:00:00~2019/8/30 12:00:00的信息"""
        result = message_query(size, start_index, start_time, end_time, state)
        result_length = len(json.loads(result)["result"])
        result_sql = get_result_from_sql()
        self.assertEqual(result_length, len(result_sql), "数据库查询日志数量为%s，调接口查询日志数量为%s" % (result_length, len(result_sql)))

    def test_share_message_query_02(self):
        """测试请求参数不传size"""
        result = message_query(size=None, start_index=start_index, start_time=start_time, end_time=end_time, state=state)
        self.assertIn('"code":0', result)

    def test_share_message_query_03(self):
        """测试请求参数不传start_index"""
        result = message_query(size=size, start_index=None, start_time=start_time, end_time=end_time, state=state)
        self.assertIn('"code":0', result)

    def test_share_message_query_04(self):
        """测试请求参数不传start_time"""
        result = message_query(size=size, start_index=start_index, start_time=None, end_time=end_time, state=state)
        self.assertIn('"code":0', result)

    def test_share_message_query_05(self):
        """测试请求参数不传end_time"""
        result = message_query(size=size, start_index=start_index, start_time=start_time, end_time=None, state=state)
        self.assertIn('"code":0', result)

    def test_share_message_query_06(self):
        """测试请求参数不传state"""
        result = message_query(size=size, start_index=start_index, start_time=start_time, end_time=end_time, state=None)
        self.assertIn('"code":0', result)

    def test_share_message_query_07(self):
        """测试请求参数都不传"""
        result = message_query(size=None, start_index=None, start_time=None, end_time=None, state=None)
        self.assertIn('"code":0', result)

    def test_share_message_query_08(self):
        """测试请求size为0"""
        result = message_query(size=0, start_index=start_index, start_time=start_time, end_time=end_time, state=state)
        self.assertIn('"code":302', result)

    def test_share_message_query_09(self):
        """测试请求size为1"""
        result = message_query(size=1, start_index=start_index, start_time=start_time, end_time=end_time, state=state)
        self.assertIn('"code":0', result)

    def test_share_message_query_10(self):
        """测试开始时间等于结束时间"""
        result = message_query(size, start_index, start_time=start_time, end_time=start_time, state=state)
        self.assertIn('"code":0', result)

    def test_share_message_query_11(self):
        """测试开始时间大于结束时间"""
        result = message_query(size, start_index, start_time=start_time, end_time=start_time.replace("2", "3"), state=None)
        self.assertIn('"code":729', result, "729：开始时间不能大于结束时间")


if __name__ == '__main__':
    unittest.main()
