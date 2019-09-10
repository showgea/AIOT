import unittest
from modules.ifttt_manage.ifttt_config.ifttt_linkage_copy import *
from common.get_result_db import get_result_from_sql
from config import readcfg

linkage_id_Gary = readcfg.linkageId_Gary
linkage_id_wrong = readcfg.linkageId_wrong
linkage_id_Jenny = readcfg.linkageId_Jenny
sql = readcfg.sql_linkageId
name = "test-ifttt5"


class TestIftttRename(unittest.TestCase):
    """
    复制一个自动化
    """
    def test_ifttt_linkage_copy_01(self):
        """测试复制一个自动化"""
        result = ifttt_linkage_copy(linkage_id_Gary, name)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_copy_02(self):
        """测试复制自动化id错误或不存在"""
        result = ifttt_linkage_copy(linkage_id_wrong, name)
        self.assertIn('"code":707', result.text)

    def test_ifttt_linkage_copy_03(self):
        """测试复制其他用户自动化"""
        result = ifttt_linkage_copy(linkage_id_Jenny, name)
        self.assertIn('"code":707', result.text)

    def test_ifttt_linkage_copy_04(self):
        """测试复制自动化id为空"""
        result = ifttt_linkage_copy("", name)
        self.assertIn('"code":302', result.text)

    def test_ifttt_linkage_copy_05(self):
        """测试重命名联动name为空"""
        result = ifttt_linkage_copy(linkage_id_Gary, "")
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
