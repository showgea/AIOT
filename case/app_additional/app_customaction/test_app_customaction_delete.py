import unittest
from modules.app_additional.app_customaction.app_customaction_delete import *


class TestAppCustomActionSet(unittest.TestCase):
    """
    删除情景模式
    """

    def test_app_customaction_delete_01(self):
        """测试删除情景模式"""
        result = app_customaction_delete("123")
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
