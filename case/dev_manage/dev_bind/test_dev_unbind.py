import unittest
from modules.dev_manage.dev_bind.dev_unbind import *
from config import readcfg

did_Gary = readcfg.did_Gary_unbind
did_Jenny = readcfg.did_Jenny_hub
unbindRule = "0000"


class TestDevUnBind(unittest.TestCase):
    """
    设备解绑
    """

    def test_dev_unbind_01(self):
        """测试设备解绑"""
        result = dev_unbind(did_Gary)
        self.assertIn('"code":706', result.text)

    def test_dev_unbind_02(self):
        """测试设备id错误或不存在"""
        result = dev_unbind(did_Gary.replace("1", "2"))
        self.assertIn('"code":706', result.text)

    def test_dev_unbind_03(self):
        """测试解绑其他用户设备"""
        result = dev_unbind(did_Jenny)
        self.assertIn('"code":706', result.text)

    def test_dev_unbind_04(self):
        """测试解绑设备id为空"""
        result = dev_unbind("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
