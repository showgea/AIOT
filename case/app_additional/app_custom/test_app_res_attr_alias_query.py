import unittest
from modules.app_additional.app_custom.app_res_attr_alias_query import *
from config import readcfg

subjectId_Gary_hub = readcfg.subjectId_Gary_hub
subjectId_Jenny = readcfg.subjectId_Jenny
subjectId_wrong = readcfg.subjectId_wrong


class TestAppResAttrAliasQuery(unittest.TestCase):
    """
    资源名称查询
    """

    def test_app_res_attr_alias_query_01(self):
        """测试资源名称查询"""
        result = app_res_attr_alias_query(subjectId_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_app_res_attr_alias_query_02(self):
        """测试查询其他用户资源名称"""
        result = app_res_attr_alias_query(subjectId_Jenny)
        self.assertIn('"code":706', result.text)

    def test_app_res_attr_alias_query_03(self):
        """测试查询设备id为空"""
        result = app_res_attr_alias_query("")
        self.assertIn('"code":302', result.text)

    def test_app_res_attr_alias_query_04(self):
        """测试查询设备id错误或不存在"""
        result = app_res_attr_alias_query(subjectId_wrong)
        self.assertIn('"code":706', result.text)


if __name__ == '__main__':
    unittest.main()
