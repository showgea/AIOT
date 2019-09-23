import unittest
from modules.positon_manage.position_query.position_query_list import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_room = readcfg.positionId_real2_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
positionType = 1
size = readcfg.size
startIndex = readcfg.startIndex


class TestPositionQueryList(unittest.TestCase):
    """
    查询用户位置结构信息，返回该位置下一级所有位置信息
    """

    def test_position_query_list_01(self):
        """测试查询home位置结构信息"""
        result = position_query_list(positionId_Gary, positionType, size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_query_list_02(self):
        """测试查询room位置信息"""
        result = position_query_list(positionId_room, positionType, size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_query_list_03(self):
        """测试查询其他用户下位置"""
        result = position_query_list(positionId_Jenny, positionType, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_position_query_list_04(self):
        """测试查询位置错误或不存在"""
        result = position_query_list(positionId_wrong, positionType, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_position_query_list_05(self):
        """测试查询位置为空"""
        result = position_query_list("", positionType, size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_query_list_06(self):
        """测试查询位置positionType为0"""
        result = position_query_list(positionId_Gary, positionType=0, size=size, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_query_list_07(self):
        """测试查询size为0"""
        result = position_query_list(positionId_Gary, positionType, size=0, startIndex=startIndex)
        self.assertIn('"code":302', result.text)

    def test_position_query_list_08(self):
        """测试请求参数不传positionId"""
        result = position_query_list(positionId=None, positionType=positionType, size=size, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_query_list_09(self):
        """测试请求参数不传positionType"""
        result = position_query_list(positionId=positionId_Gary, positionType=None, size=size, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_query_list_10(self):
        """测试请求参数不传size"""
        result = position_query_list(positionId=None, positionType=positionType, size=None, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_query_list_11(self):
        """测试请求参数不传startIndex"""
        result = position_query_list(positionId=None, positionType=positionType, size=size, startIndex=None)
        self.assertIn('"code":0', result.text)

    def test_position_query_list_12(self):
        """测试请求参数都不传"""
        result = position_query_list(positionId=None, positionType=None, size=None, startIndex=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
