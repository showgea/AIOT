import unittest
from modules.ifttt_manage.ifttt_scene_config.ifttt_scene_delete import *
from common.get_result_db import get_result_from_sql, get_all_result_from_sql

sql = readcfg.sql_sceneId
sql_Jenny = readcfg.sql_sceneId_Jenny
sceneRule = readcfg.sceneRule
sceneId_wrong = readcfg.sceneId_wrong


class TestIftttSceneDelete(unittest.TestCase):
    """
    删除场景
    """
    @classmethod
    def setUpClass(cls):
        cls.sceneId = get_all_result_from_sql(sql)
        cls.sceneId_Jenny = get_result_from_sql(sql_Jenny)[0]

    def test_ifttt_scene_delete_01(self):
        """测试删除场景"""
        for i in self.sceneId:
            print(i[0])
            result = ifttt_scene_delete(i[0], sceneRule)
            self.assertIn('"code":0', result.text)

    def test_ifttt_scene_delete_02(self):
        """测试删除场景id错误或不存在"""
        result = ifttt_scene_delete(sceneId_wrong, sceneRule)
        self.assertIn('"code":708', result.text)

    def test_ifttt_scene_delete_03(self):
        """测试删除其他用户场景"""
        result = ifttt_scene_delete(self.sceneId_Jenny, sceneRule)
        self.assertIn('"code":708', result.text)

    def test_ifttt_scene_delete_04(self):
        """测试删除id为空"""
        result = ifttt_scene_delete("", sceneRule)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
