import unittest
import json
from modules.positon_manage.position_set.position_create import *
from common.get_result_db import get_result_from_sql
from config import readcfg


positionType_0 = "0"
positionType_1 = "1"
positionName = "测试位置"
parentPositionId = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
timeZone = "+8"
remark = "position remark"
options = 0
sql = "select position_id from iot_position where user_id='38715a6d7c0608f7.606065919364653057' " \
              "ORDER BY create_time desc limit 1;"
sql_timeZone = "select time_zone from iot_position where user_id='38715a6d7c0608f7.606065919364653057'" \
      " ORDER BY create_time desc limit 1;"


class TestPositionCreate(unittest.TestCase):
    """
    创建位置
    """

    def test_position_create_01(self):
        """
        测试创建位置
        1、调用创建接口
        2、获取接口返回的position_id
        3、查询数据库中用户下最新的position_id
        4、判断是否相等
        """
        result = position_create(positionType_1, positionName, parentPositionId, timeZone, remark, options)
        position_id = json.loads(result.text)["result"]["positionId"]
        position_id_sql = get_result_from_sql(sql)[0]
        self.assertEqual(position_id, position_id_sql,
                         "创建的positionId：%s，数据库查询的positionId：%s" % (position_id, position_id_sql))

    def test_position_create_02(self):
        """测试创建位置名称已存在"""
        result = position_create(positionType_1, positionName, parentPositionId, timeZone, remark, options)
        self.assertIn('"code":703', result.text)

    def test_position_create_03(self):
        """测试创建位置时parentPositionId错误或不存在"""
        result = position_create(positionType_1, positionName, parentPositionId.replace("4", "5"), timeZone, remark, options)
        self.assertIn('"code":710', result.text)

    def test_position_create_04(self):
        """测试使用其他用户的位置为parentPositionId创建位置"""
        result = position_create_jenny(positionType_1, positionName, parentPositionId, timeZone, remark, options)
        self.assertIn('"code":710', result.text)

    def test_position_create_05(self):
        """创建虚拟位置（positionType=0）"""
        result = position_create(positionType_0, positionName=positionName + "虚拟位置", parentPositionId=None, timeZone=timeZone,
                                 remark=remark, options=options)
        position_id = json.loads(result.text)["result"]["positionId"]
        position_id_sql = get_result_from_sql(sql)[0]
        self.assertEqual(position_id, position_id_sql,
                         "创建的positionId：%s，数据库查询的positionId：%s" % (position_id, position_id_sql))

    def test_position_create_06(self):
        """测试positionType为空"""
        result = position_create("", positionName, parentPositionId=None, timeZone=timeZone, remark=remark,
                                 options=options)
        self.assertIn('"code":302', result.text)

    def test_position_create_07(self):
        """测试positionName为空"""
        result = position_create(positionType_1, "", parentPositionId=None, timeZone=timeZone, remark=remark, options=options)
        self.assertIn('"code":302', result.text)

    def test_position_create_08(self):
        """测试timeZone：-0.5"""
        result = position_create(positionType_1, positionName="测试时区", parentPositionId=None, timeZone=-0.5, remark=remark, options=options)
        time_zone_sql = get_result_from_sql(sql_timeZone)[0]
        self.assertEqual("-0.5", time_zone_sql)

    def test_position_create_09(self):
        """测试请求参数不传remark"""
        result = position_create(positionType_1, positionName + "1", parentPositionId, timeZone, remark=None,
                                 options=options)
        self.assertIn('"code":0', result.text)

    def test_position_create_10(self):
        """测试请求参数不传options"""
        result = position_create(positionType_1, positionName + "2", parentPositionId, timeZone, remark, options=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
