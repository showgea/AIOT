import unittest
from modules.res_manage.res_subscribe.res_unsubscribe import *
from config import readcfg

subjectId_Gary = readcfg.subjectId_Gary_hub
subjectId_Jenny = readcfg.subjectId_Jenny
subjectId_wrong = readcfg.subjectId_wrong
attrs = "corridor_light_status"


class TestResSubscribe(unittest.TestCase):
    """
    取消资源订阅
    """
    def test_res_unsubscribe_01(self):
        """测试取消资源订阅"""
        result = res_unsubscribe(subjectId_Gary, attrs)
        self.assertIn('"code":0', result.text)

    def test_res_unsubscribe_02(self):
        """测试取消订阅id错误或不存在"""
        result = res_unsubscribe(subjectId_wrong, attrs)
        self.assertIn('"code":756', result.text)

    def test_res_unsubscribe_03(self):
        """测试取消订阅其他人的设备id"""
        result = res_unsubscribe(subjectId_Jenny, attrs)
        self.assertIn('"code":756', result.text)

    def test_res_unsubscribe_04(self):
        """测试取消订阅设备id为空"""
        result = res_unsubscribe("", attrs)
        self.assertIn('"code":302', result.text)

    def test_res_unsubscribe_05(self):
        """测试取消订阅设备资源列表为空"""
        result = res_unsubscribe(subjectId_Gary, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
