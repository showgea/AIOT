import unittest
from modules.positon_manage.position_query.position_detail_list import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_room = readcfg.positionId_real2_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny


class TestPositionDetailList(unittest.TestCase):
    """
    查询位置详细信息
    """

    def test_position_detail_list_01(self):
        """测试查询home位置详细信息"""
        result = position_detail_list(positionId_Gary)
        self.assertIn('"code":0', result.text)

    def test_position_detail_list_02(self):
        """测试查询room位置详细信息"""
        result = position_detail_list(positionId_room)
        self.assertIn('"code":0', result.text)

    def test_position_detail_list_03(self):
        """测试查询多个位置详细信息"""
        result = position_detail_list(positionId_Gary + ',' + positionId_room)
        self.assertIn('"code":0', result.text)

    def test_position_detail_list_04(self):
        """测试查询其他用户下的位置"""
        result = position_detail_list(positionId_Jenny)
        self.assertIn('"code":710', result.text)

    def test_position_detail_list_05(self):
        """测试查询位置错误或不存在"""
        result = position_detail_list(positionId_Gary.replace("4", "5"))
        self.assertIn('"code":710', result.text)

    def test_position_detail_list_06(self):
        """测试查询位置为空"""
        result = position_detail_list("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
