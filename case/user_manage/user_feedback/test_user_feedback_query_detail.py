import unittest
from modules.user_manage.user_feedback.user_feedback_query_detail import *

feedbackId = "FB.611159953679773696"
feedbackId_wrong = "FB.611159953679773697"


class TestUserFeedbackQueryDetail(unittest.TestCase):
    """
    查看用户反馈详情
    """
    def test_user_feedback_query_detail_01(self):
        """测试查看用户反馈详情"""
        result = user_feedback_query_detail(feedbackId)
        self.assertIn('"code":0', result.text)

    def test_user_feedback_query_detail_02(self):
        """测试查看反馈id错误或不存在"""
        result = user_feedback_query_detail(feedbackId_wrong)
        self.assertIn('"code":0', result.text)

    def test_user_feedback_query_detail_03(self):
        """测试查看反馈id为空"""
        result = user_feedback_query_detail("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
