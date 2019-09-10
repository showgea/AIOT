import unittest
from modules.user_manage.user_feedback.user_feedback_query_detail import *

feedbackId = "FB.611159953679773696"


class TestUserFeedbackQueryDetail(unittest.TestCase):
    """
    查看用户反馈详情
    """
    def test_user_feedback_query_detail_01(self):
        """测试查看用户反馈详情"""
        result = user_feedback_query_detail(feedbackId)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
