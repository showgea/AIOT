import unittest
import json
from modules.user_manage.user_feedback.user_feedback_query_list import *


class TestUserFeedbackQueryList(unittest.TestCase):
    """
    查看用户反馈列表
    """
    def test_user_feedback_query_list_01(self):
        """测试查看用户反馈列表"""
        result = user_feedback_query_list()
        list_len = len(json.loads(result.text)["result"]["feedbackList"])
        self.assertGreater(list_len, 1, "用户反馈列表数量为：%s" % list_len)


if __name__ == '__main__':
    unittest.main()
