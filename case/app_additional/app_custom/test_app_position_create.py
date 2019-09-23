import unittest
import json
from modules.app_additional.app_custom.app_position_create import *
from common.get_result_db import get_result_from_sql

positionName = readcfg.position_name
parentPositionId = readcfg.positionId_real1_Gary
positionId_wrong = readcfg.positionId_wrong
positionId_Jenny = readcfg.positionId_real1_Jenny
sql = readcfg.sql_position_create
sql_timeZone = readcfg.sql_position_create_timeZone
timeZone = readcfg.timeZone
# 默认为0。 0：否；1：是，默认房间
isDefault = 0
options = 0


class TestAppPositionCreate(unittest.TestCase):
    """
    app创建位置
    """

    def test_app_position_create_01(self):
        """
        测试app创建位置-real2
        """
        result = app_position_create(positionName, parentPositionId, timeZone, isDefault, options)
        position_id = json.loads(result.text)["result"]["roomId"]
        position_id_sql = get_result_from_sql(sql)[0]
        self.assertEqual(position_id, position_id_sql,
                         "创建的positionId：%s，数据库查询的positionId：%s" % (position_id, position_id_sql))

    def test_app_position_create_02(self):
        """
        测试app创建位置-real1
        """
        result = app_position_create(positionName, parentPositionId=None, timeZone=timeZone, isDefault=isDefault,
                                     options=options)
        position_id = json.loads(result.text)["result"]["roomId"]
        position_id_sql = get_result_from_sql(sql)[0]
        self.assertEqual(position_id, position_id_sql,
                         "创建的positionId：%s，数据库查询的positionId：%s" % (position_id, position_id_sql))

    def test_app_position_create_03(self):
        """测试创建位置名称已存在"""
        result = app_position_create(positionName, parentPositionId, timeZone, isDefault, options)
        self.assertIn('"code":703', result.text)

    def test_app_position_create_04(self):
        """测试创建位置时parentPositionId错误或不存在"""
        result = app_position_create(positionName, positionId_wrong, timeZone, isDefault, options)
        self.assertIn('"code":710', result.text)

    def test_app_position_create_05(self):
        """测试使用其他用户的位置为parentPositionId创建位置"""
        result = app_position_create_jenny(positionName, positionId_Jenny, timeZone, isDefault, options)
        self.assertIn('"code":710', result.text)

    def test_app_position_create_06(self):
        """测试positionName为空"""
        result = app_position_create("", positionId_Jenny, timeZone, isDefault, options)
        self.assertIn('"code":302', result.text)

    def test_app_position_create_07(self):
        """测试timeZone：-0.5"""
        result = app_position_create(positionName + "1", parentPositionId=None, timeZone="-0.5", isDefault=isDefault,
                                     options=options)
        time_zone_sql = get_result_from_sql(sql_timeZone)[0]
        self.assertEqual("-0.5", time_zone_sql)


if __name__ == '__main__':
    unittest.main()
