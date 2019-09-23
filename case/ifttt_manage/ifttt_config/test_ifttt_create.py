import unittest
import json
from modules.ifttt_manage.ifttt_config.ifttt_create import *
from config import readcfg

name = readcfg.ifttt_name
positionId_real1_Gary = readcfg.positionId_real1_Gary
positionId_real1_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong


class TestIftttCreate(unittest.TestCase):
    """
    创建联动
    """
    def test_ifttt_create_01(self):
        """测试创建联动"""
        result = ifttt_create(name, positionId_real1_Gary)
        linkageId = json.loads(result.text)["result"]["linkageId"]
        self.assertIn('"code":0', result.text, "创建的自动化id：%s" % linkageId)

    def test_ifttt_create_02(self):
        """测试创建联动-位置错误或不存在"""
        result = ifttt_create(name, positionId_wrong)
        self.assertIn('"code":710', result.text)

    def test_ifttt_create_03(self):
        """测试创建联动-使用其他用户位置"""
        result = ifttt_create(name, positionId_real1_Jenny)
        self.assertIn('"code":710', result.text)

    def test_ifttt_create_04(self):
        """测试创建联动-位置id为空"""
        result = ifttt_create(name, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
