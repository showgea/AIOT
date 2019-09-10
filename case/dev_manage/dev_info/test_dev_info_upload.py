import unittest
from modules.dev_manage.dev_info.dev_info_upload import *
from config import readcfg

did_Gary_hub = readcfg.did_Gary_hub
did_Gary_cube = readcfg.did_Gary_cube
did_Jenny = readcfg.did_Jenny_hub
name = "魔方控制器5"


class TestDevInfoUpload(unittest.TestCase):
    """
    更新设备基本信息
    """

    def test_dev_info_upload_01(self):
        """测试更新设备名称"""
        result = dev_info_upload(did_Gary_cube, name)
        self.assertIn('"code":0', result.text)

    def test_dev_info_upload_02(self):
        """测试设备id错误或不存在"""
        result = dev_info_upload(did_Gary_cube.replace("2", "3"), name)
        self.assertIn('"code":706', result.text)

    def test_dev_info_upload_03(self):
        """测试更新其他用户下设备信息"""
        result = dev_info_upload(did_Jenny, name)
        self.assertIn('"code":706', result.text)

    def test_dev_info_upload_04(self):
        """测试设备id为空"""
        result = dev_info_upload("", name)
        self.assertIn('"code":302', result.text)

    def test_dev_info_upload_05(self):
        """测试更新设备name为空"""
        result = dev_info_upload(did_Gary_cube, "")
        self.assertIn('"code":302', result.text)

    def test_dev_info_upload_06(self):
        """测试请求参数不传非必填name"""
        result = dev_info_upload(did_Gary_cube, name=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
