import unittest
from modules.user_manage.notice_center.user_notice_read import *

msgId = "AC130001000A55F963028A64904C6DA0"
msgIds = "AC130001000A55F963028A64904C6DA0, AC130001000A55F963028A4C733567B2"


class TestUserNoticeRead(unittest.TestCase):
    """
    将通知消息的未读状态更改为已读状态
    """
    def test_user_notice_query_list_01(self):
        """测试将一条通知消息的未读状态更改为已读状态"""
        result = user_notice_read(msgId)
        self.assertIn('"code":0', result.text)

    def test_user_notice_query_list_02(self):
        """测试将多条通知消息的未读状态更改为已读状态"""
        result = user_notice_read(msgIds)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
