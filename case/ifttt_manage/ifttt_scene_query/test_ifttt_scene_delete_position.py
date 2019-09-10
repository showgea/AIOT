import unittest
from modules.ifttt_manage.ifttt_scene_query.ifttt_scene_delete_position import *
from config import readcfg

positionId_real1_Gary = readcfg.positionId_real1_Gary
positionId_real2_Gary = readcfg.positionId_real2_Gary
positionId_real1_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
deleteLabel = readcfg.deleteLabel


class TestIftttSceneDeletePosition(unittest.TestCase):
    """
    根据位置信息删除自动化或者场景执行日志
    """
    def test_ifttt_scene_delete_position_01(self):
        """测试删除单个位置场景执行日志"""
        result = ifttt_scene_delete_position(positionId_real1_Gary, deleteLabel)
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_delete_position_02(self):
        """测试删除多个位置场景执行日志"""
        result = ifttt_scene_delete_position(positionId_real1_Gary + "," + positionId_real2_Gary, deleteLabel)
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_delete_position_03(self):
        """测试删除多个位置场景执行日志中有一个位置id错误或不存在"""
        result = ifttt_scene_delete_position(positionId_real1_Gary + "," + positionId_wrong, deleteLabel)
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_delete_position_04(self):
        """测试删除多个位置场景执行日志中多个位置id错误或不存在"""
        result = ifttt_scene_delete_position(positionId_real1_Jenny + "," + positionId_wrong, deleteLabel)
        self.assertIn('"code":710', result.text)

    def test_ifttt_scene_delete_position_05(self):
        """测试删除单个位置场景执行日志-位置id错误"""
        result = ifttt_scene_delete_position(positionId_wrong, deleteLabel)
        self.assertIn('"code":710', result.text)

    def test_ifttt_scene_delete_position_06(self):
        """测试位置id为空"""
        result = ifttt_scene_delete_position("", deleteLabel)
        self.assertIn('"code":302', result.text)

    def test_ifttt_scene_delete_position_07(self):
        """测试deleteLabel为空"""
        result = ifttt_scene_delete_position(positionId_real1_Gary, "")
        self.assertIn('"code":302', result.text)

    def test_ifttt_scene_delete_position_08(self):
        """测试删除单个位置自动化执行日志"""
        result = ifttt_scene_delete_position(positionId_real1_Gary, deleteLabel="ifttt")
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_delete_position_09(self):
        """测试删除多个位置自动化执行日志"""
        result = ifttt_scene_delete_position(positionId_real1_Gary + "," + positionId_real2_Gary, deleteLabel="ifttt")
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_delete_position_10(self):
        """测试删除单个位置自动化和场景执行日志"""
        result = ifttt_scene_delete_position(positionId_real1_Gary, deleteLabel="both")
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_delete_position_11(self):
        """测试删除多个位置自动化和场景执行日志"""
        result = ifttt_scene_delete_position(positionId_real1_Gary + "," + positionId_real2_Gary, deleteLabel="both")
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
