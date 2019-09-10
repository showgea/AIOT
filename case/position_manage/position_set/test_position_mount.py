import unittest
from modules.positon_manage.position_set.position_mount import *
from config import readcfg


parentPositionId_Gary = readcfg.positionId_virtual_Gary
parentPositionId_Jenny = readcfg.positionId_virtual_Jenny
positionId_Gary = readcfg.positionId_real1_Gary
positionIds_Jenny = readcfg.positionId_real1_Jenny


class TestPositionMount(unittest.TestCase):
    """
    位置挂载
    """
    def test_position_mount_01(self):
        """测试位置挂载"""
        result = position_mount(parentPositionId_Gary, positionId_Gary)
        self.assertIn('"code":0', result.text)

    def test_position_mount_02(self):
        """测试需要挂载位置的上级位置错误或不存在"""
        result = position_mount(parentPositionId_Gary + "1", positionId_Gary)
        self.assertIn('"code":710', result.text)

    def test_position_mount_03(self):
        """测试需要挂载位置的上级位置为其他用户下的位置"""
        result = position_mount(parentPositionId_Jenny, positionId_Gary)
        self.assertIn('"code":710', result.text)

    def test_position_mount_04(self):
        """测试需要挂载位置的上级位置为空"""
        result = position_mount("", positionId_Gary)
        self.assertIn('"code":302', result.text)

    def test_position_mount_05(self):
        """测试需要挂载的位置错误或不存在"""
        result = position_mount(parentPositionId_Gary, positionId_Gary + "1")
        self.assertIn('"code":710', result.text)

    def test_position_mount_06(self):
        """测试需要挂载的位置为其他用户下的位置"""
        result = position_mount(parentPositionId_Gary, positionIds_Jenny)
        self.assertIn('"code":710', result.text)

    def test_position_mount_07(self):
        """测试需要挂载的位置为空"""
        result = position_mount(parentPositionId_Gary, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
