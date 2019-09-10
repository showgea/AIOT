import unittest
import json
from modules.dev_manage.dev_info.dev_query_detail import *
from config import readcfg

did_Gary = readcfg.did_Gary_hub
did_Gary_cube = readcfg.did_Gary_cube
did_Jenny = readcfg.did_Jenny_hub


class TestDevQueryDetail(unittest.TestCase):
    """
    查看设备详情
    """

    def test_dev_query_detail_01(self):
        """测试查看设备详情"""
        result = dev_query_detail(did_Gary)
        self.assertIn('"code":0', result.text)

    def test_dev_query_detail_02(self):
        """测试查看多个设备详情"""
        result = dev_query_detail(did_Gary + "," + did_Gary_cube)
        self.assertIn('"code":0', result.text)

    def test_dev_query_detail_03(self):
        """测试查看多个设备中有设备id错误或不存在"""
        result = dev_query_detail(did_Gary + "," + did_Gary_cube.replace("2", "3"))
        self.assertIn('"code":0', result.text)

    def test_dev_query_detail_04(self):
        """测试查看多个设备中有其他用户设备"""
        result = dev_query_detail(did_Gary + "," + did_Jenny)
        self.assertIn('"code":0', result.text)

    def test_dev_query_detail_05(self):
        """测试查看设备为空"""
        result = dev_query_detail("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
