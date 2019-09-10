import unittest
from modules.dev_manage.dev_info.dev_lock_query import *
from config import readcfg

did_Gary_hub = readcfg.did_Gary_hub
did_Gary_cube = readcfg.did_Gary_cube
did_Jenny = readcfg.did_Jenny_hub
# 1指纹 2密码 3电子锁
type_ = 1


class TestDevLockQuery(unittest.TestCase):
    """
    锁指纹密码信息查询
    """

    def test_dev_lock_query_01(self):
        """测试锁指纹密码信息查询"""
        result = dev_lock_query(did_Gary_hub, type_)
        self.assertIn('"code":0', result.text)

    def test_dev_lock_query_02(self):
        """测试id错误或不存在"""
        result = dev_lock_query(did_Gary_hub.replace("2", "3"), type_)
        self.assertIn('"code":706', result.text)

    def test_dev_lock_query_03(self):
        """测试其他用户锁指纹密码信息查询"""
        result = dev_lock_query(did_Jenny, type_)
        self.assertIn('"code":706', result.text)

    def test_dev_lock_query_04(self):
        """测试id为空"""
        result = dev_lock_query("", type_)
        self.assertIn('"code":302', result.text)

    def test_dev_lock_query_05(self):
        """测试type为空"""
        result = dev_lock_query(did_Gary_hub, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
