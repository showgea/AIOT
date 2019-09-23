import unittest
import json
from modules.dev_manage.dev_bind.dev_bindkey import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong


class TestDevBindKey(unittest.TestCase):
    """
    设备直入网bindKey获取（APP获取bindKey）
    """
    def test_dev_bindkey_01(self):
        """测试设备直入网bindKey获取"""
        result = dev_bindkey(positionId_Gary)
        bindKey = json.loads(result.text)["result"]["bindKey"]
        self.assertIn('"code":0', result.text, "获取的bindKey：%s" % bindKey)

    def test_dev_bindkey_02(self):
        """测试id错误或不存在"""
        result = dev_bindkey(positionId_wrong)
        self.assertIn('"code":710', result.text)

    def test_dev_bindkey_03(self):
        """测试从其他用户位置获取bindKey"""
        result = dev_bindkey(positionId_Jenny)
        self.assertIn('"code":710', result.text)

    def test_dev_bindkey_04(self):
        """测试id为空"""
        result = dev_bindkey("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
