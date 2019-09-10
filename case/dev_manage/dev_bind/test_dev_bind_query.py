import unittest
import json
from modules.dev_manage.dev_bind.dev_bind_query import *
from config import readcfg

bindKey_Gary = readcfg.bindKey_Gary


class TestDevBindQuery(unittest.TestCase):
    """
    设备入网结果查询
    """

    def test_dev_bind_query_01(self):
        """测试设备入网结果查询"""
        result = dev_bind_query(bindKey_Gary)
        self.assertIn('"code":0', result.text)

    def test_dev_bind_query_02(self):
        """测试bindKey错误或不存在"""
        result = dev_bind_query(bindKey_Gary + "1")
        code = json.loads(result.text)["result"]["code"]
        self.assertEqual(2, code)

    def test_dev_bind_query_03(self):
        """测试bindKey为空"""
        result = dev_bind_query("")
        code = json.loads(result.text)["result"]["code"]
        self.assertEqual(2, code)


if __name__ == '__main__':
    unittest.main()
