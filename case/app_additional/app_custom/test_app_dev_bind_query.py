import unittest
from modules.app_additional.app_custom.app_dev_bind_query import *
from config import readcfg

did_Gary_hub = readcfg.did_Gary_hub
did_Gary_cube = readcfg.did_Gary_cube
did_Jenny = readcfg.did_Jenny_hub
did_Gary_nobind = readcfg.did_Gary_nobind
did_wrong = readcfg.did_wrong


class TestAppDevBindQuery(unittest.TestCase):
    """
    查询设备绑定状态
    """

    def test_app_dev_bind_query_01(self):
        """测试查询多个设备绑定状态-多个设备都已绑定"""
        result = app_dev_bind_query(did_Gary_hub + "," + did_Gary_cube)
        self.assertIn('"code":0', result.text)

    def test_app_dev_bind_query_02(self):
        """测试查询多个设备中绑定状态-有其中一个未绑定"""
        result = app_dev_bind_query(did_Gary_hub + "," + did_Gary_nobind)
        self.assertIn('"code":0', result.text)

    def test_app_dev_bind_query_03(self):
        """测试查询多个设备中绑定状态-多个设备都未绑定"""
        result = app_dev_bind_query(did_Gary_nobind + "," + did_Gary_nobind)
        self.assertIn('"code":0', result.text)

    def test_app_dev_bind_query_04(self):
        """测试查询多个设备中绑定状态-已经被别的用户绑定"""
        result = app_dev_bind_query(did_Jenny + "," + did_Jenny)
        self.assertIn('"code":0', result.text)

    def test_app_dev_bind_query_05(self):
        """测试查询单个已绑定设备"""
        result = app_dev_bind_query(did_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_app_dev_bind_query_06(self):
        """测试查询被别的用户绑定的设备"""
        result = app_dev_bind_query(did_Jenny)
        self.assertIn('"code":0', result.text)

    def test_app_dev_bind_query_07(self):
        """测试查询未绑定的设备"""
        result = app_dev_bind_query(did_Gary_nobind)
        self.assertIn('"code":0', result.text)

    def test_app_dev_bind_query_08(self):
        """测试查询设备id错误或不存在"""
        result = app_dev_bind_query(did_wrong)
        self.assertIn('"code":0', result.text)

    def test_app_dev_bind_query_09(self):
        """测试查询设备id为空"""
        result = app_dev_bind_query("")
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
