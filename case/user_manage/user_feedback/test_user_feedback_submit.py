import unittest
from modules.user_manage.user_feedback.user_feedback_submit import *

# 0：提建议； 1：想咨询；2：提问题
type_0 = "0"
type_1 = "0"
type_2 = "0"
title = "TestTitle"
content = "TestContent"
attachFileUrls = "['url']"
contactInfo = "18682246872"


class TestUserFeedbackSubmit(unittest.TestCase):
    """
    用户反馈提交
    """

    def test_user_feedback_submit_01(self):
        """测试用户提建议"""
        result = user_feedback_submit(type_0, title + "建议", content + "建议", attachFileUrls, contactInfo)
        self.assertIn('"code":0', result.text)

    def test_user_feedback_submit_02(self):
        """测试用户想咨询"""
        result = user_feedback_submit(type_1, title + "咨询", content + "咨询", attachFileUrls, contactInfo)
        self.assertIn('"code":0', result.text)

    def test_user_feedback_submit_03(self):
        """测试用户提问题"""
        result = user_feedback_submit(type_2, title + "问题", content + "问题", attachFileUrls, contactInfo)
        self.assertIn('"code":0', result.text)

    def test_user_feedback_submit_04(self):
        """测试type为空"""
        result = user_feedback_submit("", title, content, attachFileUrls, contactInfo)
        self.assertIn('"code":302', result.text)

    def test_user_feedback_submit_05(self):
        """测试title为空"""
        result = user_feedback_submit(type_2, "", content, attachFileUrls, contactInfo)
        self.assertIn('"code":302', result.text)

    def test_user_feedback_submit_06(self):
        """测试content为空"""
        result = user_feedback_submit(type_2, title, "", attachFileUrls, contactInfo)
        self.assertIn('"code":302', result.text)

    def test_user_feedback_submit_07(self):
        """测试不传非必填项attachFileUrls"""
        result = user_feedback_submit(type_2, title, content, attachFileUrls=None, contactInfo=contactInfo)
        self.assertIn('"code":0', result.text)

    def test_user_feedback_submit_08(self):
        """测试不传非必填项contactInfo"""
        result = user_feedback_submit(type_2, title, content, attachFileUrls, contactInfo=None)
        self.assertIn('"code":0', result.text)

    def test_user_feedback_submit_09(self):
        """测试不传非必填项attachFileUrls和contactInfo"""
        result = user_feedback_submit(type_2, title, content, attachFileUrls=None, contactInfo=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
