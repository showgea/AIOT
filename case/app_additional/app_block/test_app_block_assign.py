import unittest
from modules.app_additional.app_block.app_block_assign import *
from config import readcfg

positionId_real1_Gary = readcfg.positionId_real1_Gary
positionId_real1_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
serviceId_on = readcfg.serviceId_on
serviceId_wrong = readcfg.serviceId_wrong


class TestAppBlockAssign(unittest.TestCase):
    """
   画板修改blocks,全量修改
    """

    def test_app_block_assign_01(self):
        """测试画板修改block"""
        result = app_block_assign(positionId_real1_Gary, serviceId_on)
        self.assertIn('"code":0', result.text)

    def test_app_block_assign_02(self):
        """测试修改其他用户画板block"""
        result = app_block_assign(positionId_real1_Jenny, serviceId_on)
        self.assertIn('"code":710', result.text)

    def test_app_block_assign_03(self):
        """测试对象id错误"""
        result = app_block_assign(positionId_wrong, serviceId_wrong)
        self.assertIn('"code":710', result.text)

    def test_app_block_assign_04(self):
        """测试对象id为空"""
        result = app_block_assign("", serviceId_on)
        self.assertIn('"code":302', result.text)

    def test_app_block_assign_05(self):
        """测试serviceID错误"""
        result = app_block_assign(positionId_real1_Gary, serviceId_wrong)
        self.assertIn('"code":709', result.text)

    def test_app_block_assign_06(self):
        """测试serviceID为空"""
        result = app_block_assign("", serviceId_wrong)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
