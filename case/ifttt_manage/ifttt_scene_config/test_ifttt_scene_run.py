import unittest
from modules.ifttt_manage.ifttt_scene_config.ifttt_scene_run import *
from config import readcfg

sceneId_Gary = readcfg.sceneId_Gary
sceneId_Jenny = readcfg.sceneId_Jenny
sceneId_wrong = readcfg.sceneId_wrong


class TestIftttSceneRun(unittest.TestCase):
    """
    执行场景
    """
    def test_ifttt_scene_run_01(self):
        """测试执行场景"""
        result = ifttt_scene_run(sceneId_Gary)
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_run_02(self):
        """测试执行场景id错误或不存在"""
        result = ifttt_scene_run(sceneId_wrong)
        self.assertIn('"code":708', result.text)

    def test_ifttt_scene_run_03(self):
        """测试执行其他用户场景"""
        result = ifttt_scene_run(sceneId_Jenny)
        self.assertIn('"code":708', result.text)

    def test_ifttt_scene_run_04(self):
        """测试打开联动id为空"""
        result = ifttt_scene_run("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
