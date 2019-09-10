import unittest
import json
from modules.user_manage.user_info.user_query_info import *


class TestUserQueryInfo(unittest.TestCase):
    """
    获取用户基本信息
    """
    def test_user_query_info_01(self):
        """测试获取基本信息"""
        result = user_query_info()
        nick_name = json.loads(result.text)["result"]["nickName"]
        self.assertIn("Gary", nick_name)


if __name__ == '__main__':
    unittest.main()
