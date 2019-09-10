import unittest
from modules.positon_manage.position_set.position_delete import *
from common.get_result_db import get_result_from_sql, get_all_result_from_sql
from config import readcfg


sql_gary = "select position_id from iot_position where user_id='38715a6d7c0608f7.606065919364653057' " \
              "ORDER BY create_time;"
sql_jenny = "select position_id from iot_position where user_id='649952c246de69f5.564773671348994049' " \
              "ORDER BY create_time desc limit 1;"


class TestPositionDelete(unittest.TestCase):
    """
    删除位置
    """
    @classmethod
    def setUpClass(cls):
        cls.positionId_Gary = get_all_result_from_sql(sql_gary)
        cls.positionId_Jenny = readcfg.positionId_real1_Jenny

    def test_position_delete_01(self):
        """测试删除位置"""
        for i in self.positionId_Gary:
            print(i[0])
            result = position_delete(i[0])
            self.assertIn('"code":0', result)

    def test_position_delete_02(self):
        """测试删除其他用户位置"""
        result = position_delete(self.positionId_Jenny)
        self.assertIn('"code":710', result)

    def test_position_delete_03(self):
        """测试删除位置错误或不存在"""
        result = position_delete(self.positionId_Jenny.replace("4", "5"))
        self.assertIn('"code":710', result)

    def test_position_delete_04(self):
        """测试删除位置为空"""
        result = position_delete("")
        self.assertIn('"code":302', result)


if __name__ == '__main__':
    unittest.main()
