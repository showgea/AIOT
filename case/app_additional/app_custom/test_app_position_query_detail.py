import unittest
from modules.app_additional.app_custom.app_position_query_detail import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_room = readcfg.positionId_real2_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong


class TestAppPositionQueryDetail(unittest.TestCase):
    """
    APP定制位置详情查询
    """

    def test_app_position_query_detail_01(self):
        """测试APP定制位置详情查询"""
        result = app_position_query_detail(positionId_Gary)
        self.assertIn('"code":0', result.text)

    def test_app_position_query_detail_02(self):
        """测试查询room位置详细信息"""
        result = app_position_query_detail(positionId_room)
        self.assertIn('"code":0', result.text)

    def test_app_position_query_detail_03(self):
        """测试查询其他用户下的位置"""
        result = app_position_query_detail(positionId_Jenny)
        self.assertIn('"code":710', result.text)

    def test_app_position_query_detail_04(self):
        """测试查询位置错误或不存在"""
        result = app_position_query_detail(positionId_wrong)
        self.assertIn('"code":710', result.text)

    def test_app_position_query_detail_05(self):
        """测试查询位置为空"""
        result = app_position_query_detail("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
