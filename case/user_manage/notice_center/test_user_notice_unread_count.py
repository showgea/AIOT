import unittest
from modules.user_manage.notice_center.user_notice_unread_count import *


class TestUserNoticeRead(unittest.TestCase):
    """
    获取用户的未读通知数目
    """
    def test_user_notice_query_list_01(self):
        """测试用户获取未读通知数目"""
        result = user_notice_unread_count()
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
