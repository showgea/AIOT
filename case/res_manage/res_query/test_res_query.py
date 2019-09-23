import unittest
from modules.res_manage.res_query.res_query import *
from config import readcfg

subjectId_Gary = readcfg.subjectId_Gary_cube
subjectId_Jenny = readcfg.subjectId_Jenny
subjectId_wrong = readcfg.subjectId_wrong
options = "cube_status"


class TestResQuery(unittest.TestCase):
    """
    查询设备当前资源
    """

    def test_res_query_01(self):
        """测试查询用户魔方控制器的当前资源"""
        result = res_query(subjectId_Gary, options)
        self.assertIn('"code":0', result.text)

    def test_res_query_02(self):
        """测试查询设备Id错误或不存在的当前资源"""
        result = res_query(subjectId_wrong, options)
        self.assertIn('"code":755', result.text)

    def test_res_query_03(self):
        """测试查询设备id为空"""
        result = res_query("", options)
        self.assertIn('"code":302', result.text)

    def test_res_query_04(self):
        """测试查询资源列表为空"""
        result = res_query(subjectId_Gary, "")
        self.assertIn('"code":0', result.text)

    def test_res_query_05(self):
        """测试查询其他人的设备id"""
        result = res_query(subjectId_Jenny, options)
        self.assertIn('"code":755', result.text)


if __name__ == '__main__':
    unittest.main()
