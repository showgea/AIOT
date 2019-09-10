import unittest
from modules.user_manage.notice_center.user_notice_delete import *

msgId = "AC130001000A55F963028A64904C6DA0"
msgIds = "AC130001000A55F963028A64904C6DA0, AC130001000A55F963028A4C733567B2"


class TestUserNoticeDelete(unittest.TestCase):
    """
    删除指定通知消息
    """
    def test_user_notice_query_list_01(self):
        """测试删除指定通知消息"""
        result = user_notice_delete(msgId)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_02(self):
        """测试删除多条通知消息"""
        result = user_notice_delete(msgIds)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
