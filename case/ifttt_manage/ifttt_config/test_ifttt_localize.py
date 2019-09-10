import unittest
from modules.ifttt_manage.ifttt_config.ifttt_localize import *


class TestIftttUpdate(unittest.TestCase):
    """
    所有云端自动化尝试重新本地化。
    本接口为异步执行，并不返回具体哪个成功或失败的结果（主要是因为项目账号下自动化多的情况下可能会超时）
    且一个账号一分钟内只能调用一次
    """
    def test_ifttt_localize_01(self):
        """测试云端自动化尝试重新本地化"""
        result = ifttt_localize()
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
