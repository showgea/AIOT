import unittest
from modules.family_share.relation_remark import *
from config import readcfg

account_Gary = readcfg.account_Gary
account_Jenny = readcfg.account_Jenny
remark = "test share remark"


class TestRelationRemark(unittest.TestCase):
    """
    host用户修改关联用户备注信息
    """
    def test_relation_remark_01(self):
        """测试host用户修改关联用户备注信息"""
        result = relation_remark(account_Jenny, remark)
        self.assertIn('"code":0', result.text)

    def test_relation_remark_02(self):
        """测试host用户修改自己备注信息"""
        result = relation_remark(account_Gary, remark)
        self.assertIn('"code":821', result.text, "不支持给自己设置备注")

    def test_relation_remark_03(self):
        """测试修改账号未注册"""
        result = relation_remark(account_Gary.replace("2", "1"), remark)
        self.assertIn('"code":801', result.text, "账号未注册")

    def test_relation_remark_04(self):
        """测试必填项账号为空"""
        result = relation_remark("", remark)
        self.assertIn('"code":302', result.text)

    def test_relation_remark_05(self):
        """测试必填项remark为空"""
        result = relation_remark(account_Gary, "")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
