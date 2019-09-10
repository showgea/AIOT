import unittest
from modules.dev_manage.dev_bind.dev_bind_user import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
did_Gary = readcfg.did_Gary_hub
did_Jenny = readcfg.did_Jenny_hub
# 0：不发网关  1：发网关，默认为1
isSendGateway = 1


class TestDevBindUser(unittest.TestCase):
    """
    网关绑定用户
    """

    def test_dev_bind_user_01(self):
        """测试网关绑定用户"""
        result = dev_bind_user(did_Gary, positionId_Gary, isSendGateway)
        self.assertIn('"code":607', result.text)

    def test_dev_bind_user_02(self):
        """测试网关id错误或不存在"""
        result = dev_bind_user(did_Gary.replace("1", "2"), positionId_Gary, isSendGateway)
        self.assertIn('"code":601', result.text)

    def test_dev_bind_user_03(self):
        """测试绑定其他用户网关"""
        result = dev_bind_user(did_Jenny, positionId_Gary, isSendGateway)
        self.assertIn('"code":603', result.text)

    def test_dev_bind_user_04(self):
        """测试网关绑定到其他用户下位置"""
        result = dev_bind_user(did_Gary, positionId_Jenny, isSendGateway)
        self.assertIn('"code":710', result.text)

    def test_dev_bind_user_05(self):
        """测试不发网关"""
        result = dev_bind_user(did_Gary, positionId_Gary, isSendGateway=0)
        self.assertIn('"code":607', result.text)

    def test_dev_bind_user_06(self):
        """测试请求参数不传isSendGateway"""
        result = dev_bind_user(did_Gary, positionId_Gary, isSendGateway=None)
        self.assertIn('"code":607', result.text)


if __name__ == '__main__':
    unittest.main()
