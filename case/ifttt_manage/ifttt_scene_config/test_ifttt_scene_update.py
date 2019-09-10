import unittest
from modules.ifttt_manage.ifttt_scene_config.ifttt_scene_update import *

name = "开夜灯5"


class TestIftttSceneUpdate(unittest.TestCase):
    """
    更新场景
    """
    def test_ifttt_scene_update_01(self):
        """测试更新场景"""
        result = ifttt_scene_update(name)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
