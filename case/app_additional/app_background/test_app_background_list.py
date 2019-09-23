import unittest
from modules.app_additional.app_background.app_background_list import *


class TestAppBackgroundList(unittest.TestCase):
    """
   查询系统壁纸列表
    """

    def test_app_background_list_01(self):
        """测试查询系统壁纸列表"""
        result = app_background_list()
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
