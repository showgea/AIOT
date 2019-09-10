import unittest
import json
from modules.family_share.share_invite import *
from common.get_result_db import get_unreply_share_id
from config import readcfg


positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
account_Gary = readcfg.account_Gary
account_Jenny = readcfg.account_Jenny
permission = 3
hint = "hint"
remark = "test invite remark"


class TestShareInvite(unittest.TestCase):
    """
    邀请成员加入位置分享
    """

    def test_share_invite_01(self):
        """测试邀请成员加入位置分享"""
        result = share_invite_after_remove(positionId_Gary, account_Jenny, permission, hint, remark)
        share_id_api = json.loads(result)["result"]["shareId"]
        share_id_sql = get_unreply_share_id()
        self.assertEqual(share_id_api, share_id_sql, "接口返回share_id：%s，数据库中查询share_id：%s" % (share_id_api, share_id_sql))

    def test_share_invite_02(self):
        """测试分享的位置已分享"""
        result = share_invite(positionId_Gary, account_Jenny, permission, hint, remark)
        self.assertIn('"code":2206', result.text, "This position has invite")

    def test_share_invite_03(self):
        """测试邀请账号未注册"""
        result = share_invite(positionId_Gary, account_Jenny + "1", permission, hint, remark)
        self.assertIn('"code":801', result.text, "账号未注册")

    def test_share_invite_04(self):
        """测试邀请账号为空"""
        result = share_invite(positionId_Gary, "", permission, hint, remark)
        self.assertIn('"code":302', result.text)

    def test_share_invite_05(self):
        """测试邀请位置错误或不存在"""
        result = share_invite(positionId_Gary.replace("4", "5"), account_Jenny, permission, hint, remark)
        self.assertIn('"code":710', result.text)

    def test_share_invite_06(self):
        """测试使用其他用户的位置进行邀请"""
        result = share_invite(positionId_Jenny, account_Jenny, permission, hint, remark)
        self.assertIn('"code":710', result.text)

    def test_share_invite_07(self):
        """测试邀请位置为空"""
        result = share_invite("", account_Jenny, permission, hint, remark)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
