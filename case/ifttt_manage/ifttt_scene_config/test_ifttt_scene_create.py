import unittest
import json
from modules.ifttt_manage.ifttt_scene_config.ifttt_scene_create import *
from config import readcfg

positionId_real1_Gary = readcfg.positionId_real1_Gary
positionId_real1_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
subjectId_Gary_hub = readcfg.subjectId_Gary_hub
subjectId_Jenny = readcfg.subjectId_Jenny
subjectId_wrong = readcfg.subjectId_wrong
name = readcfg.scene_name


class TestIftttSceneCreate(unittest.TestCase):
    """
    创建场景
    """
    def test_ifttt_scene_create_01(self):
        """测试创建场景"""
        result = ifttt_scene_create(positionId_real1_Gary, name, subjectId_Gary_hub)
        sceneId = json.loads(result.text)["result"]["sceneId"]
        self.assertIn('"code":0', result.text, "创建的场景id：%s" % sceneId)

    def test_ifttt_scene_create_02(self):
        """测试位置id错误或不存在"""
        result = ifttt_scene_create(positionId_wrong, name, subjectId_Gary_hub)
        self.assertIn('"code":710', result.text)

    def test_ifttt_scene_create_03(self):
        """测试使用其他用户位置id"""
        result = ifttt_scene_create(positionId_real1_Jenny, name, subjectId_Gary_hub)
        self.assertIn('"code":710', result.text)

    def test_ifttt_scene_create_04(self):
        """测试位置id为空"""
        result = ifttt_scene_create("", name, subjectId_Gary_hub)
        self.assertIn('"code":302', result.text)

    def test_ifttt_scene_create_05(self):
        """测试设备id错误或不存在"""
        result = ifttt_scene_create(positionId_real1_Gary, name, subjectId_wrong)
        self.assertIn('"code":706', result.text)

    def test_ifttt_scene_create_06(self):
        """测试使用其他用户设备id"""
        result = ifttt_scene_create(positionId_real1_Gary, name, subjectId_Jenny)
        self.assertIn('"code":706', result.text)

    def test_ifttt_scene_create_07(self):
        """测试设备id为空"""
        result = ifttt_scene_create(positionId_real1_Gary, name, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
