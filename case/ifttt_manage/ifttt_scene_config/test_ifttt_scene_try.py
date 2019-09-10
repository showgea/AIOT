import unittest
from modules.ifttt_manage.ifttt_scene_config.ifttt_scene_try import *


class TestIftttSceneTry(unittest.TestCase):
    """
    试一下执行场景
    """
    def test_ifttt_scene_try_01(self):
        """测试试一下执行场景"""
        result = ifttt_scene_try()
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
