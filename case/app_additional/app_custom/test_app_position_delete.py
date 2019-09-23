import unittest
from modules.app_additional.app_custom.app_position_delete import *
from common.get_result_db import get_all_result_from_sql

sql = readcfg.sql_position_delete


class TestAppPositionDelete(unittest.TestCase):
    """
    app删除位置
    """
    @classmethod
    def setUpClass(cls):
        cls.positionId_Gary = get_all_result_from_sql(sql)
        cls.positionId_Jenny = readcfg.positionId_real1_Jenny
        cls.positionId_wrong = readcfg.positionId_wrong

    def test_app_position_delete_01(self):
        """测试app删除位置"""
        for i in self.positionId_Gary:
            # print(i[0])
            result = app_position_delete(i[0])
            self.assertIn('"code":0', result)

    def test_app_position_delete_02(self):
        """测试删除其他用户位置"""
        result = app_position_delete(self.positionId_Jenny)
        self.assertIn('"code":710', result)

    def test_app_position_delete_03(self):
        """测试删除位置错误或不存在"""
        result = app_position_delete(self.positionId_wrong)
        self.assertIn('"code":710', result)

    def test_app_position_delete_04(self):
        """测试删除位置为空"""
        result = app_position_delete("")
        self.assertIn('"code":302', result)


if __name__ == '__main__':
    unittest.main()
