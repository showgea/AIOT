import unittest
from modules.family_share.share_query import *
from config import readcfg


position_id_Gary = readcfg.positionId_real1_Gary
position_id_Jenny = readcfg.positionId_real1_Jenny


class TestShareQuery(unittest.TestCase):
    """
    查询该位置分享的基本信息
    """

    def test_share_query_01(self):
        """测试查询用户下的家的基本信息"""
        result = share_query(position_id_Gary)
        self.assertIn('"code":0', result.text)

    def test_share_query_02(self):
        """测试查询位置无权限"""
        result = share_query(position_id_Jenny)
        self.assertIn('"code":710', result.text)

    def test_share_query_03(self):
        """测试查询位置错误或不存在"""
        result = share_query(position_id_Gary.replace("4", "5"))
        self.assertIn('"code":710', result.text)

    def test_share_query_04(self):
        """测试查询位置为空"""
        result = share_query("")
        self.assertIn('"code":302', result.text, "查询位置为空时，应该为302：请求参数错误")


if __name__ == '__main__':
    unittest.main()
