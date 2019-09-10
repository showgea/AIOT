import unittest
from modules.positon_manage.position_based_query.position_gateway_query import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
size = 10
startIndex = 0


class TestPositionGatewayQuery(unittest.TestCase):
    """
    查询属于某个位置下的网关信息
    """

    def test_position_gateway_query_01(self):
        """测试查询用户自己的家下面位置的网关信息"""
        result = position_gateway_query(positionId_Gary, size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_gateway_query_02(self):
        """测试查询位置错误或不存在"""
        result = position_gateway_query(positionId_Gary.replace("2", "3"), size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_position_gateway_query_03(self):
        """测试查询其他用户下位置"""
        result = position_gateway_query(positionId_Jenny, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_position_gateway_query_04(self):
        """测试请求参数size为0"""
        result = position_gateway_query(positionId_Gary, size=0, startIndex=startIndex)
        self.assertIn('"code":302', result.text)

    def test_position_gateway_query_05(self):
        """测试请求参数size为1"""
        result = position_gateway_query(positionId_Gary, size=1, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_gateway_query_06(self):
        """测试请求参数不传size"""
        result = position_gateway_query(positionId_Gary, size=None, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_gateway_query_07(self):
        """测试请求参数不传startIndex"""
        result = position_gateway_query(positionId_Gary, size, startIndex=None)
        self.assertIn('"code":0', result.text)

    def test_position_gateway_query_08(self):
        """测试请求参数不传size和startIndex"""
        result = position_gateway_query(positionId_Gary, size=None, startIndex=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
