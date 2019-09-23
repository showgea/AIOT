import unittest
from modules.app_additional.app_custom.app_dev_close_alarm import *
from config import readcfg

linkageId_Gary = readcfg.linkageId_Gary
linkageId_Jenny = readcfg.linkageId_Jenny
linkageId_wrong = readcfg.linkageId_wrong


class TestAppDevCloseAlarm(unittest.TestCase):
    """
    取消告警
    """
    def test_app_dev_close_alarm_01(self):
        """测试取消告警"""
        result = app_dev_close_alarm(linkageId_Gary)
        self.assertIn('"code":0', result)

    def test_app_dev_close_alarm_02(self):
        """测试取消其他用户告警"""
        result = app_dev_close_alarm(linkageId_Jenny)
        self.assertIn('"code":707', result)

    def test_app_dev_close_alarm_03(self):
        """测试取消告警id错误或不存在"""
        result = app_dev_close_alarm(linkageId_wrong)
        self.assertIn('"code":707', result)

    def test_app_dev_close_alarm_04(self):
        """测试取消告警id为空"""
        result = app_dev_close_alarm("")
        self.assertIn('"code":302', result)


if __name__ == '__main__':
    unittest.main()
