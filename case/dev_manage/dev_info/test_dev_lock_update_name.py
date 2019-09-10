import unittest
from modules.dev_manage.dev_info.dev_lock_update_name import *
from config import readcfg

did_Gary_hub = readcfg.did_Gary_hub
did_Gary_cube = readcfg.did_Gary_cube
did_Jenny = readcfg.did_Jenny_hub
typeValue = "65537"
typeName = "xxx"


class TestDevLockUpdateName(unittest.TestCase):
    """
    锁指纹密码名称修改
    """

    def test_dev_lock_update_name_01(self):
        """测试锁指纹密码名称修改"""
        result = dev_lock_update_name(did_Gary_hub, typeValue, typeName)
        self.assertIn('"code":0', result.text)

    def test_dev_lock_update_name_02(self):
        """测试id错误或不存在"""
        result = dev_lock_update_name(did_Gary_hub.replace("2", "3"), typeValue, typeName)
        self.assertIn('"code":706', result.text)

    def test_dev_lock_update_name_03(self):
        """测试修改其他用户锁指纹密码名称"""
        result = dev_lock_update_name(did_Jenny, typeValue, typeName)
        self.assertIn('"code":706', result.text)

    def test_dev_lock_update_name_04(self):
        """测试id为空"""
        result = dev_lock_update_name("", typeValue, typeName)
        self.assertIn('"code":302', result.text)

    def test_dev_lock_update_name_05(self):
        """测试typeValue为空"""
        result = dev_lock_update_name(did_Gary_hub, "", typeName)
        self.assertIn('"code":302', result.text)

    def test_dev_lock_update_name_06(self):
        """测试typeName为空"""
        result = dev_lock_update_name(did_Gary_hub, typeValue, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
