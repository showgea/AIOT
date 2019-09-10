import unittest
from modules.family_share.relation_query import *
from config import readcfg

account_Gary = readcfg.account_Gary
account_Jenny = readcfg.account_Jenny


class TestRelationQuery(unittest.TestCase):
    """
    查询用户关联的信息
    """

    def test_relation_query_01(self):
        """测试查询其他用户的信息"""
        result = relation_query(account_Jenny)
        self.assertIn('"nickName":"Jenny"', result.text)

    def test_relation_query_02(self):
        """测试查询自己的信息"""
        result = relation_query(account_Gary)
        self.assertIn('"nickName":"Gary"', result.text)

    def test_relation_query_03(self):
        """测试查询账号错误或不存在"""
        result = relation_query(account_Gary.replace("2", "1"))
        self.assertIn('"code":801', result.text, "账号未注册")

    def test_relation_query_04(self):
        """测试查询账号为空"""
        result = relation_query("")
        self.assertIn('"code":302', result.text, "查询账号为空，应该返回302：Params error")


if __name__ == '__main__':
    unittest.main()
