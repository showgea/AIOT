import unittest
from modules.app_additional.app_block.app_block_remove import *
from config import readcfg

positionId_real1_Gary = readcfg.positionId_real1_Gary
positionId_real1_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
serviceId_wrong = readcfg.serviceId_wrong


class TestAppBlockRemove(unittest.TestCase):
    """
   画板移除block
    """

    def test_app_block_remove_01(self):
        """测试画板移除block"""
        result = app_block_remove(positionId_real1_Gary, serviceId_wrong)
        self.assertIn('"code":0', result.text)

    def test_app_block_remove_02(self):
        """测试对其他用户画板移除block"""
        result = app_block_remove(positionId_real1_Jenny, serviceId_wrong)
        self.assertIn('"code":710', result.text)

    def test_app_block_remove_03(self):
        """测试对象id错误"""
        result = app_block_remove(positionId_wrong, serviceId_wrong)
        self.assertIn('"code":710', result.text)

    def test_app_block_remove_04(self):
        """测试对象id为空"""
        result = app_block_remove("", serviceId_wrong)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
