import unittest
from modules.ifttt_manage.ifttt_scene_query.ifttt_scene_query_detail import *
from config import readcfg

sceneId_Gary = readcfg.sceneId_Gary
sceneId_Jenny = readcfg.sceneId_Jenny
sceneId_wrong = readcfg.sceneId_wrong


class TestIftttSceneQueryDetail(unittest.TestCase):
    """
    查找场景的详细信息
    """

    def test_ifttt_scene_query_detail_01(self):
        """测试查找场景的详细信息"""
        result = ifttt_scene_query_detail(sceneId_Gary)
        self.assertIn('"code":0', result.text)

    def test_ifttt_scene_query_detail_02(self):
        """测试查询场景id错误或不存在"""
        result = ifttt_scene_query_detail(sceneId_wrong)
        self.assertIn('"code":708', result.text)

    def test_ifttt_scene_query_detail_03(self):
        """测试查询其他用户场景详细信息"""
        result = ifttt_scene_query_detail(sceneId_Jenny)
        self.assertIn('"code":708', result.text)

    def test_ifttt_scene_query_detail_04(self):
        """测试查询场景id为空"""
        result = ifttt_scene_query_detail("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
