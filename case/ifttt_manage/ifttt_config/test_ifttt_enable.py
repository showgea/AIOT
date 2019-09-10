import unittest
from modules.ifttt_manage.ifttt_config.ifttt_enable import *
from config import readcfg

linkage_id_Gary = readcfg.linkageId_Gary
linkage_id_wrong = readcfg.linkageId_wrong
linkage_id_Jenny = readcfg.linkageId_Jenny
# 0：关闭；1：打开
enable = 1


class TestIftttEnable(unittest.TestCase):
    """
    打开/关闭联动
    """
    def test_ifttt_enable_01(self):
        """测试打开联动"""
        result = ifttt_enable(linkage_id_Gary, enable)
        self.assertIn('"code":0', result.text)

    def test_ifttt_enable_02(self):
        """测试关闭联动"""
        result = ifttt_enable(linkage_id_Gary, 0)
        self.assertIn('"code":0', result.text)

    def test_ifttt_enable_03(self):
        """测试打开联动id错误或不存在"""
        result = ifttt_enable(linkage_id_wrong, enable)
        self.assertIn('"code":707', result.text)

    def test_ifttt_enable_04(self):
        """测试打开其他用户联动"""
        result = ifttt_enable(linkage_id_Jenny, enable)
        self.assertIn('"code":707', result.text)

    def test_ifttt_enable_05(self):
        """测试打开联动id为空"""
        result = ifttt_enable("", enable)
        self.assertIn('"code":302', result.text)

    def test_ifttt_enable_06(self):
        """测试关闭联动id为空"""
        result = ifttt_enable("", 0)
        self.assertIn('"code":302', result.text)

    def test_ifttt_enable_07(self):
        """测试enable输入为空"""
        result = ifttt_enable(linkage_id_Gary, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
