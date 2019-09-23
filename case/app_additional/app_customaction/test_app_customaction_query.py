import unittest
from modules.app_additional.app_customaction.app_customaction_query import *
from config import readcfg

did_Gary_hub = readcfg.did_Gary_hub
did_Jenny_hub = readcfg.did_Jenny_hub
did_wrong = readcfg.did_wrong
hub_Model = readcfg.hub_Model
actionId = "scene_mode"


class TestAppCustomActionQuery(unittest.TestCase):
    """
    查询情景模式
    """

    def test_app_customaction_query_01(self):
        """测试查询情景模式"""
        result = app_customaction_query(did_Gary_hub, hub_Model, actionId)
        self.assertIn('"code":0', result.text)

    def test_app_customaction_query_02(self):
        """测试查询其他用户绑定设备id的情景模式"""
        result = app_customaction_query(did_Jenny_hub, hub_Model, actionId)
        self.assertIn('"code":706', result.text)

    def test_app_customaction_query_03(self):
        """测试查询设备id错误或不存在"""
        result = app_customaction_query(did_wrong, hub_Model, actionId)
        self.assertIn('"code":706', result.text)

    def test_app_customaction_query_04(self):
        """测试查询设备id为空"""
        result = app_customaction_query("", hub_Model, actionId)
        self.assertIn('"code":302', result.text)

    def test_app_customaction_query_05(self):
        """测试设备类型id为空"""
        result = app_customaction_query(did_Gary_hub, "", actionId)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
