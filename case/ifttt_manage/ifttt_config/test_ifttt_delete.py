import unittest
from modules.ifttt_manage.ifttt_config.ifttt_delete import *
from common.get_result_db import get_result_from_sql
from config import readcfg

sql = readcfg.sql_linkageId
sql_Jenny = readcfg.sql_linkageId_Jenny
linkageRule = readcfg.linkageRule


class TestIftttDelete(unittest.TestCase):
    """
    删除联动
    """
    @classmethod
    def setUpClass(cls):
        cls.linkageId = get_result_from_sql(sql)[0]
        cls.linkageId_Jenny = get_result_from_sql(sql_Jenny)[0]

    def test_ifttt_delete_01(self):
        """测试删除联动"""
        result = ifttt_delete(self.linkageId, linkageRule)
        self.assertIn('"code":0', result.text)

    def test_ifttt_delete_02(self):
        """测试删除联动id错误或不存在"""
        result = ifttt_delete(self.linkageId + "1", linkageRule)
        self.assertIn('"code":707', result.text)

    def test_ifttt_delete_03(self):
        """测试删除其他用户的联动"""
        result = ifttt_delete(self.linkageId_Jenny, linkageRule)
        self.assertIn('"code":707', result.text)

    def test_ifttt_delete_04(self):
        """测试删除联动id为空"""
        result = ifttt_delete("", linkageRule)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
