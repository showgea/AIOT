import unittest
import json
from modules.service_manage.service_attribute.service_name_fuzzy import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
name = "灯"


class TestServiceNameFuzzy(unittest.TestCase):
    """
    serviceName模糊查询
    """

    def test_service_name_fuzzy_01(self):
        """测试serviceName模糊查询"""
        result = service_name_fuzzy(positionId_Gary, name)
        self.assertIn('"code":0', result.text)

    def test_service_name_fuzzy_02(self):
        """测试位置id错误或不存在"""
        result = service_name_fuzzy(positionId_wrong, name)
        self.assertIn('"code":710', result.text)

    def test_service_name_fuzzy_03(self):
        """测试使用其他用户下位置id"""
        result = service_name_fuzzy(positionId_Jenny, name)
        self.assertIn('"code":710', result.text)

    def test_service_name_fuzzy_04(self):
        """测试位置id为空"""
        result = service_name_fuzzy("", name)
        self.assertIn('"code":302', result.text)

    def test_service_name_fuzzy_05(self):
        """测试Service名称不存在"""
        result = service_name_fuzzy(positionId_Gary, name="testname")
        length = len(json.loads(result.text)["result"])
        self.assertEqual(0, length)

    def test_service_name_fuzzy_06(self):
        """测试Service名称为空"""
        result = service_name_fuzzy(positionId_Gary, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
