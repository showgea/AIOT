import unittest
from modules.app_additional.app_background.app_background_set import *
from config import readcfg

positionId_real1_Gary = readcfg.positionId_real1_Gary
positionId_real1_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong


class TestAppBackgroundSet(unittest.TestCase):
    """
   设置用户壁纸或房间壁纸
    """

    def test_app_background_set_01(self):
        """测试设置用户壁纸或房间壁纸"""
        result = app_background_set(positionId_real1_Gary)
        self.assertIn('"code":0', result.text)

    def test_app_background_set_02(self):
        """测试设置位置id属于其他用户"""
        result = app_background_set(positionId_real1_Jenny)
        self.assertIn('"code":710', result.text)

    def test_app_background_set_03(self):
        """测试设置位置id错误"""
        result = app_background_set(positionId_wrong)
        self.assertIn('"code":710', result.text)

    def test_app_background_set_04(self):
        """测试不传位置id"""
        result = app_background_set(positionId=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
