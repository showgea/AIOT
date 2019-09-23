import unittest
from modules.app_additional.app_block.app_block_query import *
from config import readcfg

positionId_real1_Gary = readcfg.positionId_real1_Gary
positionId_real1_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong


class TestAppBlockAssign(unittest.TestCase):
    """
   画板信息查询
    """

    def test_app_block_query_01(self):
        """测试画板信息查询"""
        result = app_block_query(positionId_real1_Gary)
        self.assertIn('"code":0', result.text)

    def test_app_block_query_02(self):
        """测试查询其他用户画板信息"""
        result = app_block_query(positionId_real1_Jenny)
        self.assertIn('"code":710', result.text)

    def test_app_block_query_03(self):
        """测试对象id错误"""
        result = app_block_query(positionId_wrong)
        self.assertIn('"code":710', result.text)

    def test_app_block_query_04(self):
        """测试对象id为空"""
        result = app_block_query("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
