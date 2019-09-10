import unittest
from modules.ifttt_manage.ifttt_scene_config.ifttt_scene_rename import *

sceneId_Gary = readcfg.sceneId_Gary
sceneId_Jenny = readcfg.sceneId_Jenny
sceneId_wrong = readcfg.sceneId_wrong
name = "开夜灯55"


class TestIftttSceneRename(unittest.TestCase):
    """
    重命名场景
    """
    def test_ifttt_scene_rename_01(self):
        """测试重命名场景"""
        result = ifttt_scene_rename(sceneId_Gary, name)
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_rename_02(self):
        """测试场景id错误或不存在"""
        result = ifttt_scene_rename(sceneId_wrong, name)
        self.assertIn('"code":708', result.text)

    def test_ifttt_scene_rename_03(self):
        """测试重命名其他用户的场景"""
        result = ifttt_scene_rename(sceneId_Jenny, name)
        self.assertIn('"code":708', result.text)

    def test_ifttt_scene_rename_04(self):
        """测试场景id为空"""
        result = ifttt_scene_rename("", name)
        self.assertIn('"code":302', result.text)

    def test_ifttt_scene_rename_05(self):
        """测试重命名新的场景名称为空"""
        result = ifttt_scene_rename(sceneId_Gary, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
