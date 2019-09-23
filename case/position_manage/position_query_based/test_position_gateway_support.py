import unittest
from modules.positon_manage.position_based_query.position_gateway_support import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
model = " lumi.light.aqcn02"
size = readcfg.size
startIndex = readcfg.startIndex


class TestPositionGatewaySupport(unittest.TestCase):
    """
    添加子设备时查询当前位置下的支持网关列表
    """

    def test_position_gateway_support_01(self):
        """测试查询用户自己的家下面位置支持的网关列表"""
        result = position_gateway_support(positionId_Gary, model, size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_gateway_support_02(self):
        """测试查询位置错误或不存在"""
        result = position_gateway_support(positionId_wrong, model, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_position_gateway_support_03(self):
        """测试查询其他用户下位置"""
        result = position_gateway_support(positionId_Jenny, model, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_position_gateway_support_04(self):
        """测试请求参数size为0"""
        result = position_gateway_support(positionId_Gary, model, size=0, startIndex=startIndex)
        self.assertIn('"code":302', result.text)

    def test_position_gateway_support_05(self):
        """测试请求参数size为1"""
        result = position_gateway_support(positionId_Gary, model, size=1, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_gateway_support_06(self):
        """测试请求参数不传size"""
        result = position_gateway_support(positionId_Gary, model, size=None, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_gateway_support_07(self):
        """测试请求参数不传startIndex"""
        result = position_gateway_support(positionId_Gary, model, size, startIndex=None)
        self.assertIn('"code":0', result.text)

    def test_position_gateway_support_08(self):
        """测试请求参数不传size和startIndex"""
        result = position_gateway_support(positionId_Gary, model, size=None, startIndex=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
