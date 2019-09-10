import unittest
from modules.ifttt_manage.ifttt_scene_query.ifttt_scene_query_list import *
from config import readcfg

subjectId_Gary_hub = readcfg.subjectId_Gary_hub
subjectId_Jenny = readcfg.subjectId_Jenny
subjectId_wrong = readcfg.subjectId_wrong


class TestIftttSceneQueryList(unittest.TestCase):
    """
    根据设备查询场景列表
    """

    def test_ifttt_scene_query_list_01(self):
        """测试根据设备查询场景列表"""
        result = ifttt_scene_query_list(subjectId_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_query_list_02(self):
        """测试设备id错误或不存在"""
        result = ifttt_scene_query_list(subjectId_wrong)
        self.assertIn('"code":706', result.text)

    def test_ifttt_scene_query_list_03(self):
        """测试查询其他用户设备的联动列表"""
        result = ifttt_scene_query_list(subjectId_Jenny)
        self.assertIn('"code":706', result.text)

    def test_ifttt_scene_query_list_04(self):
        """测试设备id为空"""
        result = ifttt_scene_query_list("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
