import unittest
from modules.ifttt_manage.ifttt_scene_config.ifttt_scene_icon_update import *

sceneId_Gary = readcfg.sceneId_Gary
sceneId_Jenny = readcfg.sceneId_Jenny
sceneId_wrong = readcfg.sceneId_wrong
iconId = readcfg.iconId


class TestIftttSceneIconUpdate(unittest.TestCase):
    """
    更换场景图片
    """
    def test_ifttt_scene_icon_update_01(self):
        """测试更换场景图片"""
        result = ifttt_scene_icon_update(sceneId_Gary, iconId)
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_icon_update_02(self):
        """测试更换场景id错误或不存在"""
        result = ifttt_scene_icon_update(sceneId_wrong, iconId)
        self.assertIn('"code":708', result.text)

    def test_ifttt_scene_icon_update_03(self):
        """测试更换其他用户的场景图片"""
        result = ifttt_scene_icon_update(sceneId_Jenny, iconId)
        self.assertIn('"code":708', result.text)

    def test_ifttt_scene_icon_update_04(self):
        """测试更换场景id为空"""
        result = ifttt_scene_icon_update("", iconId)
        self.assertIn('"code":302', result.text)

    def test_ifttt_scene_icon_update_05(self):
        """测试更换场景图片iconId错误或不存在"""
        result = ifttt_scene_icon_update(sceneId_Gary, iconId + "1")
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_icon_update_06(self):
        """测试更换场景图片iconId为空"""
        result = ifttt_scene_icon_update(sceneId_Gary, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
