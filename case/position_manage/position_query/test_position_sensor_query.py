import unittest
from modules.positon_manage.position_query.position_sensor_query import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_room = readcfg.positionId_real2_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny


class TestPositionSensorQuery(unittest.TestCase):
    """
    位置软传感查询
    """
    def test_position_sensor_query_01(self):
        """位置软传感查询"""
        result = position_sensor_query(positionId_Gary)
        self.assertIn('"code":732', result.text)

    def test_position_sensor_query_02(self):
        """测试查询位置出错误或不存在"""
        result = position_sensor_query(positionId_Gary + "1")
        self.assertIn('"code":710', result.text)

    def test_position_sensor_query_03(self):
        """测试查询其他用户下的位置"""
        result = position_sensor_query(positionId_Jenny)
        self.assertIn('"code":710', result.text)

    def test_position_sensor_query_04(self):
        """测试查询位置为空"""
        result = position_sensor_query("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
