import unittest
import json
from modules.positon_manage.position_based_query.position_device_assign_query import *

dids = "lumi.158d0003930b2a,lumi.158d00026e9e32"
dids_Jenny = "virtual.38136362841914"


class TestPositionDeviceAssignQuery(unittest.TestCase):
    """
    查询指定的设备属于哪个位置，可以传入多个设备id
    """

    def test_position_device_assign_query_01(self):
        """测试查询多个设备属于的位置"""
        result = position_device_assign_query(dids)
        length = len(json.loads(result.text)["result"])
        self.assertEqual(2, length)

    def test_position_device_assign_query_02(self):
        """测试查询多个设备中有一个设备id错误或不存在"""
        result = position_device_assign_query(dids + "1")
        length = len(json.loads(result.text)["result"])
        self.assertEqual(1, length)

    def test_position_device_assign_query_03(self):
        """测试查询多个设备id都错误或不存在"""
        result = position_device_assign_query(dids.replace("1", "2"))
        self.assertIn('"code":706', result.text)

    def test_position_device_assign_query_04(self):
        """测试查询设备为空"""
        result = position_device_assign_query("")
        self.assertIn('"code":302', result.text)

    def test_position_device_assign_query_05(self):
        """测试查询其他用户下的设备"""
        result = position_device_assign_query(dids_Jenny)
        self.assertIn('"code":706', result.text)


if __name__ == '__main__':
    unittest.main()
