import unittest
from modules.dev_manage.dev_info.dev_children_query import *
from config import readcfg

did_Gary_hub = readcfg.did_Gary_hub
did_Gary_cube = readcfg.did_Gary_cube
did_Jenny = readcfg.did_Jenny_hub


class TestDevChildrenQuery(unittest.TestCase):
    """
    查询网关下子设备信息
    """

    def test_dev_children_query_01(self):
        """测试查询网关下子设备信息"""
        result = dev_children_query(did_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_dev_children_query_02(self):
        """测试查看设备id错误或不存在"""
        result = dev_children_query(did_Gary_hub.replace("2", "3"))
        self.assertIn('"code":706', result.text)

    def test_dev_children_query_03(self):
        """测试查询其他用户网关下子设备信息"""
        result = dev_children_query(did_Jenny)
        self.assertIn('"code":706', result.text)

    def test_dev_children_query_04(self):
        """测试网关设备id为空"""
        result = dev_children_query("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
