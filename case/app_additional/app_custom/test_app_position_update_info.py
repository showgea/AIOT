import unittest
from modules.app_additional.app_custom.app_position_update_info import *
from common.get_result_db import get_result_from_sql

positionId_real1_Gary = readcfg.positionId_real1_Gary2
positionId_real2_Gary = readcfg.positionId_real2_Gary2
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
positionName = readcfg.position_name
positionName_default = readcfg.position_default_name
isDefault = 0


class TestAppPositionUpdateInfo(unittest.TestCase):
    """
    更新位置基本信息
    """

    def test_app_position_update_info_01(self):
        """测试更新real1位置基本信息"""
        result = app_position_update_info(positionId_real1_Gary, positionName, isDefault)
        sql = "select name from iot_position where position_id='%s';" % positionId_real1_Gary
        position_name_sql = get_result_from_sql(sql)[0]
        self.assertEqual(positionName, position_name_sql)

    def test_app_position_update_info_02(self):
        """测试更新real2位置基本信息"""
        result = app_position_update_info(positionId_real2_Gary, positionName, isDefault)
        sql = "select name from iot_position where position_id='%s';" % positionId_real2_Gary
        position_name_sql = get_result_from_sql(sql)[0]
        self.assertEqual(positionName, position_name_sql)

    def test_app_position_update_info_03(self):
        """测试更新其他用户的位置基本信息"""
        result = app_position_update_info(positionId_Jenny, positionName, isDefault)
        self.assertIn('"code":710', result.text)

    def test_app_position_update_info_04(self):
        """测试更新的位置错误或不存在"""
        result = app_position_update_info(positionId_wrong, positionName, isDefault)
        self.assertIn('"code":710', result.text)

    def test_app_position_update_info_05(self):
        """测试请求参数不传positionName"""
        result = app_position_update_info(positionId_real2_Gary, positionName=None, isDefault=isDefault)
        self.assertIn('"code":0', result.text)

    def test_app_position_update_info_06(self):
        """测试请求参数不传isDefault"""
        result = app_position_update_info(positionId_real1_Gary, positionName_default, isDefault=None)
        self.assertIn('"code":0', result.text)

    def test_app_position_update_info_07(self):
        """测试请求参数不传isDefault"""
        result = app_position_update_info(positionId_real2_Gary, positionName_default, isDefault=None)
        self.assertIn('"code":0', result.text)

    def test_app_position_update_info_08(self):
        """测试请求参数不传positionName和isDefault"""
        result = app_position_update_info(positionId_real2_Gary, positionName=None, isDefault=None)
        self.assertIn('"code":0', result.text)

    def test_app_position_update_info_09(self):
        """测试请求参数positionId为空"""
        result = app_position_update_info("", positionName=None, isDefault=None)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
