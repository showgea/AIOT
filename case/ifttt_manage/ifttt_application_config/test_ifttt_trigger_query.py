import unittest
from modules.ifttt_manage.ifttt_application_config.ifttt_trigger_query import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
size = readcfg.size
startIndex = readcfg.startIndex


class TestIftttTriggerQuery(unittest.TestCase):
    """
    查看提供触发器的应用列表
    """

    def test_ifttt_trigger_query_01(self):
        """测试查看提供触发器的应用列表"""
        result = ifttt_trigger_query(positionId_Gary, size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_trigger_query_02(self):
        """测试位置id错误或不存在"""
        result = ifttt_trigger_query(positionId_wrong, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_ifttt_trigger_query_03(self):
        """测试查看其他用户下的位置提供触发器的应用列表"""
        result = ifttt_trigger_query(positionId_Jenny, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_ifttt_trigger_query_04(self):
        """测试位置id为空"""
        result = ifttt_trigger_query("", size, startIndex)
        self.assertIn('"code":302', result.text)

    def test_ifttt_trigger_query_05(self):
        """测试请求参数不传size"""
        result = ifttt_trigger_query(positionId_Gary, size=None, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_trigger_query_06(self):
        """测试请求参数不传startIndex"""
        result = ifttt_trigger_query(positionId_Gary, size, startIndex=None)
        self.assertIn('"code":0', result.text)

    def test_ifttt_trigger_query_07(self):
        """测试size为0"""
        result = ifttt_trigger_query(positionId_Gary, 0, startIndex)
        self.assertIn('"code":302', result.text)

    def test_ifttt_trigger_query_08(self):
        """测试size为1"""
        result = ifttt_trigger_query(positionId_Gary, 1, startIndex)
        self.assertIn('"code":0', result.text)

    def test_ifttt_trigger_query_09(self):
        """测试请求参数不传size、startIndex"""
        result = ifttt_trigger_query(positionId_Gary)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
