import unittest
from modules.ifttt_manage.ifttt_config.ifttt_rename import *
from common.get_result_db import get_result_from_sql
from config import readcfg

linkage_id_Gary = readcfg.linkageId_Gary
linkage_id_wrong = readcfg.linkageId_wrong
linkage_id_Jenny = readcfg.linkageId_Jenny
name = readcfg.ifttt_name
sql = readcfg.sql_linkageId


class TestIftttRename(unittest.TestCase):
    """
    重命名联动
    """
    @classmethod
    def setUpClass(cls):
        cls.linkageId = get_result_from_sql(sql)[0]

    def test_ifttt_rename_01(self):
        """测试重命名联动"""
        result = ifttt_rename(self.linkageId, name)
        self.assertIn('"code":0', result.text)

    def test_ifttt_rename_02(self):
        """测试重命名联动id错误或不存在"""
        result = ifttt_rename(linkage_id_wrong, name)
        self.assertIn('"code":707', result.text)

    def test_ifttt_rename_03(self):
        """测试重命名其他用户联动"""
        result = ifttt_rename(linkage_id_Jenny, name)
        self.assertIn('"code":707', result.text)

    def test_ifttt_rename_04(self):
        """测试重命名联动id为空"""
        result = ifttt_rename("", name)
        self.assertIn('"code":302', result.text)

    def test_ifttt_rename_05(self):
        """测试重命名联动name为空"""
        result = ifttt_rename(linkage_id_Gary, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
