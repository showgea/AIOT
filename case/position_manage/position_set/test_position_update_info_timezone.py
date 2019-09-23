import unittest
from modules.positon_manage.position_set.position_update_info_timezone import *
from common.get_result_db import get_result_from_sql

positionId_real1_Gary = readcfg.positionId_real1_Gary2
positionId_real2_Gary = readcfg.positionId_real2_Gary2
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
timeZone_0 = "+0"
timeZone_8 = "+8"
timeZoneCity = "tz_dublin"


class TestPositionUpdateInfoTimezone(unittest.TestCase):
    """
    修改位置时区
    """

    def test_position_update_info_timezone_01(self):
        """测试修改real1位置时区"""
        result = position_update_info_timezone(positionId_real1_Gary, timeZone_0, timeZoneCity)
        sql = "select time_zone from iot_position where position_id='%s';" % positionId_real1_Gary
        time_zone_sql = get_result_from_sql(sql)[0]
        print(time_zone_sql)
        self.assertEqual("+0", time_zone_sql)

    def test_position_update_info_timezone_02(self):
        """测试修改real2位置时区"""
        result = position_update_info_timezone(positionId_real2_Gary, timeZone_8, timeZoneCity)
        sql = "select time_zone from iot_position where position_id='%s';" % positionId_real2_Gary
        time_zone_sql = get_result_from_sql(sql)[0]
        print(time_zone_sql)
        self.assertEqual("+0", time_zone_sql)

    def test_position_update_info_timezone_03(self):
        """测试修改其他人位置的时区"""
        result = position_update_info_timezone(positionId_Jenny, timeZone_0, timeZoneCity)
        self.assertIn('"code":710', result.text)

    def test_position_update_info_timezone_04(self):
        """测试修改位置错误或不存在"""
        result = position_update_info_timezone(positionId_wrong, timeZone_0, timeZoneCity)
        self.assertIn('"code":710', result.text)

    def test_position_update_info_timezone_05(self):
        """测试positionId为空"""
        result = position_update_info_timezone("", timeZone_0, timeZoneCity=timeZoneCity)
        self.assertIn('"code":302', result.text)

    def test_position_update_info_timezone_07(self):
        """测试timeZone为空"""
        result = position_update_info_timezone(positionId_real1_Gary, "", timeZoneCity=timeZoneCity)
        self.assertIn('"code":302', result.text)

    def test_position_update_info_timezone_08(self):
        """测试不传timeZoneCity"""
        result = position_update_info_timezone(positionId_real1_Gary, timeZone_8, timeZoneCity=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
