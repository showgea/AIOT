import unittest
from modules.family_share.share_invite_reply import *


share_id = get_share_id()
# 0-拒接、1-接收，默认为0
result_1 = 1
result_0 = 0


class TestInviteReply(unittest.TestCase):
    """
    成员对邀请的位置分享进行答复
    """

    def test_share_invite_reply_01(self):
        """测试成员接受邀请位置分享"""
        res = invite_reply(share_id, result_1)
        self.assertIn('"code":0', res.text)

    def test_share_invite_reply_2(self):
        """测试邀请id错误或不存在"""
        res = invite_reply(share_id.replace("0", "1"), result_1)
        self.assertIn('"code":2202', res.text)

    def test_share_invite_reply_03(self):
        """测试邀请id为空"""
        res = invite_reply("", result_1)
        self.assertIn('"code":302', res.text)

    def test_share_invite_reply_04(self):
        """测试回复为空"""
        res = invite_reply(share_id, "")
        self.assertIn('"code":302', res.text)

    def test_share_invite_reply_05(self):
        """测试回复和邀请人为同一个人"""
        res = invite_reply_same(share_id, result_1)
        self.assertIn('"code":2201', res.text)

    def test_share_invite_reply_06(self):
        """测试邀请已经回复"""
        shareId = get_share_id()
        res = invite_reply(shareId, result_1)
        self.assertIn('"code":0', res.text)


if __name__ == '__main__':
    unittest.main()
