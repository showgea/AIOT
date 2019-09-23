import unittest
from modules.ifttt_manage.ifttt_config.ifttt_update import *
from common.get_result_db import get_result_from_sql
from config import readcfg

name = readcfg.ifttt_name
positionId_real1_Gary = readcfg.positionId_real1_Gary
positionId_real2_Gary = readcfg.positionId_real2_Gary
positionId_real1_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
sql = readcfg.sql_linkageId


class TestIftttUpdate(unittest.TestCase):
    """
    更新联动
    """
    @classmethod
    def setUpClass(cls):
        cls.linkageId = get_result_from_sql(sql)[0]

    def test_ifttt_update_01(self):
        """测试更新联动名称"""
        result = ifttt_update(self.linkageId, name, positionId_real1_Gary)
        self.assertIn('"code":0', result.text)

    def test_ifttt_update_02(self):
        """测试更新联动位置"""
        result = ifttt_update(self.linkageId, name, positionId_real2_Gary)
        self.assertIn('"code":0', result.text)

    def test_ifttt_update_03(self):
        """测试更新联动位置错误或不存在"""
        result = ifttt_update(self.linkageId, name, positionId_wrong)
        self.assertIn('"code":710', result.text)

    def test_ifttt_update_04(self):
        """测试更新联动位置属于其他用户"""
        result = ifttt_update(self.linkageId, name, positionId_real1_Jenny)
        self.assertIn('"code":710', result.text)


if __name__ == '__main__':
    unittest.main()
