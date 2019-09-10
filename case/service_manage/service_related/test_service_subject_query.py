import unittest
import json
from modules.service_manage.service_related.service_subject_query import *
from config import readcfg

subjectId_Gary = readcfg.subjectId_Gary_hub
subjectId_Gary_cube = readcfg.subjectId_Gary_cube
subjectId_Jenny = readcfg.subjectId_Jenny
subjectId_wrong = readcfg.subjectId_wrong


class TestServiceSubjectQuery(unittest.TestCase):
    """
    查询对象subjectId拥有的service基本信息
    """

    def test_service_subject_query_01(self):
        """测试查询对象subjectId拥有的service基本信息"""
        result = service_subject_query(subjectId_Gary)
        self.assertIn('"code":0', result.text)

    def test_service_subject_query_02(self):
        """测试查询多个对象subjectId拥有的service基本信息"""
        result = service_subject_query(subjectId_Gary + "," + subjectId_Gary_cube)
        length = len(json.loads(result.text)["result"])
        self.assertEqual(2, length)

    def test_service_subject_query_03(self):
        """测试查询多个对象中有subjectId错误或不存在"""
        result = service_subject_query(subjectId_Gary + "," + subjectId_wrong)
        length = len(json.loads(result.text)["result"])
        self.assertEqual(1, length)

    def test_service_subject_query_04(self):
        """测试查询多个对象中有其他用户的subjectId"""
        result = service_subject_query(subjectId_Gary + "," + subjectId_Jenny)
        length = len(json.loads(result.text)["result"])
        self.assertEqual(1, length)

    def test_service_subject_query_05(self):
        """测试查询对象subjectId错误或不存在"""
        result = service_subject_query(subjectId_wrong)
        self.assertIn('"code":709', result.text)

    def test_service_subject_query_06(self):
        """测试查询对象subjectId为空"""
        result = service_subject_query("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
