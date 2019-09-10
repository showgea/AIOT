import unittest
from modules.positon_manage.position_set.position_update_sort import *

list_ = [{"positionId": "real2.615940701667794944", "sortNo": "1"},
         {"positionId": "real2.614518677566062592", "sortNo": "2"}]


class TestPositionUpdateInfo(unittest.TestCase):
    """
    更新位置排序
    """

    def test_position_update_sort_01(self):
        """测试更新位置排序"""
        result = position_update_sort(list_)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
