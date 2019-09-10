import unittest
from modules.user_manage.user_info.user_report_info import *
from common.get_result_db import get_result_from_sql

nickName = "Gary"
gender = 0
birthday = "2018-01-01"
area = "shenzhen"
sql = "select nick_name,gender,birthday,area from iot_user where user_id='38715a6d7c0608f7.606065919364653057';"


class TestUserReportInfo(unittest.TestCase):
    """
    上传用户基本信息
    """
    def test_user_report_info_01(self):
        """测试上传用户基本信息"""
        result = user_report_info(nickName=nickName, gender=gender, birthday=birthday, area=area)
        result_from_sql = get_result_from_sql(sql)
        self.assertEqual((nickName, gender, birthday, area), result_from_sql)

    def test_user_report_info_02(self):
        """测试上传用户昵称"""
        result = user_report_info(nickName=nickName, gender=None, birthday=None, area=None)
        self.assertIn('"code":0', result.text)

    def test_user_report_info_03(self):
        """测试上传用户性别"""
        result = user_report_info(nickName=None, gender=gender, birthday=None, area=None)
        self.assertIn('"code":0', result.text)

    def test_user_report_info_04(self):
        """测试上传用户生日"""
        result = user_report_info(nickName=None, gender=None, birthday=birthday, area=None)
        self.assertIn('"code":0', result.text)

    def test_user_report_info_05(self):
        """测试上传用户地区"""
        result = user_report_info(nickName=None, gender=None, birthday=None, area=area)
        self.assertIn('"code":0', result.text)

    def test_user_report_info_06(self):
        """测试上传用户基本信息都为空"""
        result = user_report_info(nickName=None, gender=None, birthday=None, area=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
