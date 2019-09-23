import unittest
from modules.app_additional.app_customaction.app_customaction_set import *


class TestAppCustomActionSet(unittest.TestCase):
    """
    设置情景模式
    """

    def test_app_customaction_set_01(self):
        """测试设置情景模式"""
        result = app_customaction_set()
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
