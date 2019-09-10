import unittest
from modules.positon_manage.position_query.position_default_query import *


class TestPositionDefaultQuery(unittest.TestCase):
    """
    查询用户默认家
    """

    def test_position_default_query_01(self):
        """测试查询用户默认家"""
        result = position_default_query()
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
