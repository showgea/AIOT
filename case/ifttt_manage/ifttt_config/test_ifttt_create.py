import unittest
import json
from modules.ifttt_manage.ifttt_config.ifttt_create import *


class TestIftttCreate(unittest.TestCase):
    """
    创建联动
    """
    def test_ifttt_create_01(self):
        """测试创建联动"""
        result = ifttt_create()
        linkageId = json.loads(result.text)["result"]["linkageId"]
        self.assertIn('"code":0', result.text, "创建的自动化id：%s" % linkageId)


if __name__ == '__main__':
    unittest.main()
