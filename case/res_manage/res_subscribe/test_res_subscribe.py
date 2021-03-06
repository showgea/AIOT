import unittest
from modules.res_manage.res_subscribe.res_subscribe import *
from config import readcfg

subjectId_Gary = readcfg.subjectId_Gary_hub
subjectId_Jenny = readcfg.subjectId_Jenny
subjectId_wrong = readcfg.subjectId_wrong
attrs = "corridor_light_status"


class TestResSubscribe(unittest.TestCase):
    """
    订阅资源
    """
    def test_res_subscribe_01(self):
        """测试订阅资源"""
        result = res_subscribe(subjectId_Gary, attrs)
        self.assertIn('"code":0', result.text)

    def test_res_subscribe_02(self):
        """测试订阅id错误或不存在"""
        result = res_subscribe(subjectId_wrong, attrs)
        self.assertIn('"code":756', result.text)

    def test_res_subscribe_03(self):
        """测试订阅其他人的设备id"""
        result = res_subscribe(subjectId_Jenny, attrs)
        self.assertIn('"code":756', result.text)

    def test_res_subscribe_04(self):
        """测试订阅设备id为空"""
        result = res_subscribe("", attrs)
        self.assertIn('"code":302', result.text)

    def test_res_subscribe_05(self):
        """测试订阅设备资源列表为空"""
        result = res_subscribe(subjectId_Gary, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
