import unittest
from modules.app_additional.account_transfer.account_delete import *


class TestAccountDelete(unittest.TestCase):
    """
   Saas删除项目后调用清除云端清除项目token
    """

    def test_account_delete_01(self):
        """测试Saas删除项目后调用清除云端清除项目token"""
        result = account_delete("xxx", "xxx")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
