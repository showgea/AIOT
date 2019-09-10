import unittest
from modules.family_share.share_unread_count import *


class TestUnreadCount(unittest.TestCase):
    """
    分享是否存在未读消息
    """

    def test_unread_count_01(self):
        """测试Gary查询分享是否存在未读消息"""
        result = unread_count()
        self.assertIn('"code":0', result)


if __name__ == '__main__':
    unittest.main()
