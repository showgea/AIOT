import unittest
from modules.ifttt_manage.ifttt_query.ifttt_linkage_query_detail import *
from config import readcfg

linkageId_Gary = readcfg.linkageId_Gary
linkageId_Jenny = readcfg.linkageId_Jenny
linkageId_wrong = readcfg.linkageId_wrong


class TestIftttLinkageQueryDetail(unittest.TestCase):
    """
    查询联动详细信息
    """

    def test_ifttt_linkage_query_detail_01(self):
        """测试查询联动详细信息"""
        result = ifttt_linkage_query_detail(linkageId_Gary)
        self.assertIn('"code":0', result.text)

    def test_ifttt_linkage_query_detail_02(self):
        """测试查询联动id错误或不存在"""
        result = ifttt_linkage_query_detail(linkageId_wrong)
        self.assertIn('"code":707', result.text)

    def test_ifttt_linkage_query_detail_03(self):
        """测试查询其他用户的联动详细信息"""
        result = ifttt_linkage_query_detail(linkageId_Jenny)
        self.assertIn('"code":707', result.text)

    def test_ifttt_linkage_query_detail_04(self):
        """测试查询联动id为空"""
        result = ifttt_linkage_query_detail(linkageId_Jenny)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
