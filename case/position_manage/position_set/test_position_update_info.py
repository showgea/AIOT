import unittest
from modules.positon_manage.position_set.position_update_info import *
from common.get_result_db import get_result_from_sql
from config import readcfg

positionId_real1_Gary = readcfg.positionId_real1_Gary2
positionId_real2_Gary = readcfg.positionId_real2_Gary2
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
positionName = readcfg.position_name
positionName_default = readcfg.position_default_name
remark = readcfg.remark


class TestPositionUpdateInfo(unittest.TestCase):
    """
    更新位置基本信息
    """

    def test_position_update_info_01(self):
        """测试更新real1位置基本信息"""
        result = position_update_info(positionId_real1_Gary, positionName, remark)
        sql = "select name from iot_position where position_id='%s';" % positionId_real1_Gary
        position_name_sql = get_result_from_sql(sql)[0]
        self.assertEqual(positionName, position_name_sql)

    def test_position_update_info_02(self):
        """测试更新real2位置基本信息"""
        result = position_update_info(positionId_real2_Gary, positionName, remark)
        sql = "select name from iot_position where position_id='%s';" % positionId_real2_Gary
        position_name_sql = get_result_from_sql(sql)[0]
        self.assertEqual(positionName, position_name_sql)

    def test_position_update_info_03(self):
        """测试更新其他用户的位置基本信息"""
        result = position_update_info(positionId_Jenny, positionName, remark)
        self.assertIn('"code":710', result.text)

    def test_position_update_info_04(self):
        """测试更新的位置错误或不存在"""
        result = position_update_info(positionId_wrong, positionName, remark)
        self.assertIn('"code":710', result.text)

    def test_position_update_info_05(self):
        """测试更新位置名称已存在"""
        result = position_update_info(positionId_real2_Gary, positionName, remark)
        self.assertIn('"code":703', result.text)

    def test_position_update_info_06(self):
        """测试请求参数不传positionName"""
        result = position_update_info(positionId_real2_Gary, positionName=None, remark=remark)
        self.assertIn('"code":0', result.text)

    def test_position_update_info_07(self):
        """测试请求参数不传remark"""
        result = position_update_info(positionId_real1_Gary, positionName_default, remark=None)
        self.assertIn('"code":0', result.text)

    def test_position_update_info_08(self):
        """测试更新remark"""
        result = position_update_info(positionId_real2_Gary, positionName_default, remark)
        self.assertIn('"code":0', result.text)

    def test_position_update_info_09(self):
        """测试请求参数不传positionName和remark"""
        result = position_update_info(positionId_real1_Gary, positionName=None, remark=None)
        self.assertIn('"code":302', result.text)

    def test_position_update_info_10(self):
        """测试请求参数positionId为空"""
        result = position_update_info("", positionName=None, remark=None)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
