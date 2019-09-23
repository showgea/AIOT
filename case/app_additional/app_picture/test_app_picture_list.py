import unittest
from modules.app_additional.app_picture.app_picture_list import *


class TestAppPictureList(unittest.TestCase):
    """
   查询系统图片列表
    """

    def test_app_picture_list_01(self):
        """测试查询系统图片列表"""
        result = app_picture_list("package_ifttt")
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
