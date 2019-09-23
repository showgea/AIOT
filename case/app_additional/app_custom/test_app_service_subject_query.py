import unittest
from modules.app_additional.app_custom.app_service_subject_query import *
from config import readcfg

did_Gary_hub = readcfg.did_Gary_hub
did_Gary_cube = readcfg.did_Gary_cube
did_Jenny = readcfg.did_Jenny_hub
did_wrong = readcfg.did_wrong
linkageId_Gary = readcfg.linkageId_Gary
linkageId_Jenny = readcfg.linkageId_Jenny
linkageId_wrong = readcfg.linkageId_wrong
sceneId_Gary = readcfg.sceneId_Gary
sceneId_Jenny = readcfg.sceneId_Jenny
sceneId_wrong = readcfg.sceneId_wrong


class TestAppServiceSubjectQuery(unittest.TestCase):
    """
    查询对象subjectId拥有的service基本信息
    """

    def test_app_service_subject_query_01(self):
        """测试查询多个设备id拥有的service基本信息"""
        result = app_service_subject_query(did_Gary_hub + "," + did_Gary_cube)
        self.assertIn('"code":0', result.text)

    def test_app_service_subject_query_02(self):
        """测试查询多个设备id中有一个错误或不存在"""
        result = app_service_subject_query(did_Gary_hub + "," + did_wrong)
        self.assertIn('"code":0', result.text)

    def test_app_service_subject_query_03(self):
        """测试查询多个设备id错误或不存在"""
        result = app_service_subject_query(did_wrong + "," + did_wrong)
        self.assertIn('"code":755', result.text)

    def test_app_service_subject_query_04(self):
        """测试查询单个设备id拥有的service基本信息"""
        result = app_service_subject_query(did_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_app_service_subject_query_05(self):
        """测试查询其他用户的设备id拥有的service基本信息"""
        result = app_service_subject_query(did_wrong)
        self.assertIn('"code":755', result.text)

    def test_app_service_subject_query_06(self):
        """测试查询单个设备id错误或不存在"""
        result = app_service_subject_query(did_wrong)
        self.assertIn('"code":755', result.text)

    def test_app_service_subject_query_07(self):
        """测试查询单个设备id为空"""
        result = app_service_subject_query("")
        self.assertIn('"code":302', result.text)

    def test_app_service_subject_query_08(self):
        """测试查询多个自动化id拥有的service基本信息"""
        result = app_service_subject_query(linkageId_Gary + "," + linkageId_Gary)
        self.assertIn('"code":0', result.text)

    def test_app_service_subject_query_09(self):
        """测试查询多个自动化id中有一个错误或不存在"""
        result = app_service_subject_query(linkageId_Gary + "," + linkageId_wrong)
        self.assertIn('"code":0', result.text)

    def test_app_service_subject_query_10(self):
        """测试查询多个自动化id错误或不存在"""
        result = app_service_subject_query(linkageId_Jenny + "," + linkageId_wrong)
        self.assertIn('"code":755', result.text)

    def test_app_service_subject_query_11(self):
        """测试查询单个自动化id拥有的service基本信息"""
        result = app_service_subject_query(linkageId_Gary)
        self.assertIn('"code":0', result.text)

    def test_app_service_subject_query_12(self):
        """测试查询其他用户的自动化id拥有的service基本信息"""
        result = app_service_subject_query(linkageId_Jenny)
        self.assertIn('"code":755', result.text)

    def test_app_service_subject_query_13(self):
        """测试查询单个自动化id错误或不存在"""
        result = app_service_subject_query(linkageId_wrong)
        self.assertIn('"code":755', result.text)

    def test_app_service_subject_query_14(self):
        """测试查询单个自动化id为空"""
        result = app_service_subject_query("")
        self.assertIn('"code":302', result.text)

    def test_app_service_subject_query_15(self):
        """测试查询多个场景id拥有的service基本信息"""
        result = app_service_subject_query(sceneId_Gary + "," + sceneId_Gary)
        self.assertIn('"code":0', result.text)

    def test_app_service_subject_query_16(self):
        """测试查询多个场景id中有一个错误或不存在"""
        result = app_service_subject_query(sceneId_Gary + "," + sceneId_wrong)
        self.assertIn('"code":0', result.text)

    def test_app_service_subject_query_17(self):
        """测试查询多个场景id错误或不存在"""
        result = app_service_subject_query(sceneId_Jenny + "," + sceneId_wrong)
        self.assertIn('"code":755', result.text)

    def test_app_service_subject_query_18(self):
        """测试查询单个场景id拥有的service基本信息"""
        result = app_service_subject_query(sceneId_Gary)
        self.assertIn('"code":0', result.text)

    def test_app_service_subject_query_19(self):
        """测试查询其他用户的场景id拥有的service基本信息"""
        result = app_service_subject_query(sceneId_Jenny)
        self.assertIn('"code":755', result.text)

    def test_app_service_subject_query_20(self):
        """测试查询单个场景id错误或不存在"""
        result = app_service_subject_query(sceneId_wrong)
        self.assertIn('"code":755', result.text)

    def test_app_service_subject_query_21(self):
        """测试查询单个场景id为空"""
        result = app_service_subject_query("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
