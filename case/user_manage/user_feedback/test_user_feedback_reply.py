import unittest
from modules.user_manage.user_feedback.user_feedback_reply import *

feedbackId = "FB.616013401183813632"
reply = "test reply"


class TestUserFeedbackReply(unittest.TestCase):
    """
    回复反馈
    """

    def test_user_feedback_reply_01(self):
        """测试回复反馈"""
        result = user_feedback_reply(feedbackId, reply)
        self.assertIn('"code":0', result.text)

    def test_user_feedback_reply_02(self):
        """测试回复的反馈id错误或不存在"""
        result = user_feedback_reply(feedbackId + "1", reply)
        self.assertIn('"code":302', result.text)

    def test_user_feedback_reply_03(self):
        """测试回复内容为空"""
        result = user_feedback_reply(feedbackId, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
