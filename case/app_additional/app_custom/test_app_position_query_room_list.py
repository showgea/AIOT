import unittest
from modules.app_additional.app_custom.app_position_query_room_list import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_room = readcfg.positionId_real2_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
size = 100
startIndex = 0


class TestAppPositionQueryRoomoList(unittest.TestCase):
    """
    app查询用户家下的房间结构信息，返回该用户room的分页信息
    """

    def test_app_position_query_room_list_01(self):
        """测试app查询用户家下的房间结构信息"""
        result = app_position_query_room_list(positionId_Gary, startIndex, size)
        self.assertIn('"code":0', result.text)

    def test_app_position_query_room_list_02(self):
        """测试查询room位置信息"""
        result = app_position_query_room_list(positionId_room, startIndex, size)
        self.assertIn('"code":0', result.text)

    def test_app_position_query_room_list_03(self):
        """测试查询其他用户下位置"""
        result = app_position_query_room_list(positionId_Jenny, startIndex, size)
        self.assertIn('"code":710', result.text)

    def test_app_position_query_room_list_04(self):
        """测试查询位置错误或不存在"""
        result = app_position_query_room_list(positionId_wrong, startIndex, size)
        self.assertIn('"code":710', result.text)

    def test_app_position_query_room_list_05(self):
        """测试查询位置为空"""
        result = app_position_query_room_list("", startIndex, size)
        self.assertIn('"code":302', result.text)

    def test_app_position_query_room_list_06(self):
        """测试查询size为0"""
        result = app_position_query_room_list(positionId_Gary, startIndex, size=0)
        self.assertIn('"code":302', result.text)

    def test_app_position_query_room_list_07(self):
        """测试请求参数不传size"""
        result = app_position_query_room_list(positionId_Gary, startIndex, size=None)
        self.assertIn('"code":0', result.text)

    def test_app_position_query_room_list_08(self):
        """测试请求参数不传startIndex"""
        result = app_position_query_room_list(positionId_Gary, startIndex=None, size=size)
        self.assertIn('"code":0', result.text)

    def test_app_position_query_room_list_09(self):
        """测试请求参数都不传"""
        result = app_position_query_room_list(positionId_Gary, startIndex=None, size=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
