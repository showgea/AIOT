import unittest
from modules.ifttt_manage.ifttt_query.ifttt_execute_query_detail import *

executeCode = get_code()


class TestIftttExecuteQueryDetail(unittest.TestCase):
    """
    查看自动化或场景的详细执行日志
    """
    def test_ifttt_execute_query_detail_01(self):
        """测试查看自动化或场景的详细执行日志"""
        result = ifttt_execute_query_detail(executeCode)
        self.assertIn('"code":0', result.text)

    def test_ifttt_execute_query_detail_02(self):
        """测试executeCode错误或不存在"""
        result = ifttt_execute_query_detail(executeCode + "1")
        self.assertIn('"code":0', result.text)

    def test_ifttt_execute_query_detail_04(self):
        """测试executeCode为空"""
        result = ifttt_execute_query_detail("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
