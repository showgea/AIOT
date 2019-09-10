import unittest
from modules.res_manage.res_query.res_attr_alias_query import *
from config import readcfg

subjectId_Gary = readcfg.positionId_real1_Gary
subjectId_Jenny = readcfg.positionId_real1_Jenny
attrs = ["argb_value"]


class TestResAttrAliasQuery(unittest.TestCase):
    """
    资源名称查询
    """

    def test_res_attr_alias_query_01(self):
        """测试查询用户资源名称查询"""
        result = res_attr_alias_query(subjectId_Gary, attrs)
        self.assertIn('"code":0', result.text)

    def test_res_attr_alias_query_02(self):
        """测试查询id错误或不存在"""
        result = res_attr_alias_query(subjectId_Gary.replace("1", "2"), attrs)
        self.assertIn('"code":755', result.text)

    def test_res_attr_alias_query_03(self):
        """测试查询id为空"""
        result = res_attr_alias_query("", attrs)
        self.assertIn('"code":302', result.text)

    def test_res_attr_alias_query_04(self):
        """测试查询其他人的id"""
        result = res_attr_alias_query(subjectId_Jenny, attrs)
        self.assertIn('"code":755', result.text)


if __name__ == '__main__':
    unittest.main()
