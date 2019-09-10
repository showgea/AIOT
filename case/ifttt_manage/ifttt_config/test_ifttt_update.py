import unittest
from modules.ifttt_manage.ifttt_config.ifttt_update import *


class TestIftttUpdate(unittest.TestCase):
    """
    更新联动
    """
    def test_ifttt_update_01(self):
        """测试更新联动"""
        result = ifttt_update()
        self.assertIn('"code":707', result.text)


if __name__ == '__main__':
    unittest.main()
