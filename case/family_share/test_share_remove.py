import unittest
from modules.family_share.share_remove import *


share_id = get_share_id()


class TestShareRemove(unittest.TestCase):
    """
    取消位置分享
    """

    def test_invite_remove_01(self):
        """测试host取消位置分享"""
        shareId = get_share_id()
        res = share_remove(shareId)
        self.assertIn('"code":0', res.text)

    def test_invite_remove_02(self):
        """测试分享已经取消后，host再进行remove"""
        res = share_remove(share_id)
        self.assertIn('"code":2203', res.text, "邀请消息已失效")

    def test_invite_remove_03(self):
        """测试被邀请人未回复前，被邀请人进行remove"""
        global shareId
        shareId = get_share_id()
        res = share_remove_jenny(shareId)
        self.assertIn('"code":2201', res.text, "被邀请人没有权限这么操作")

    def test_invite_remove_04(self):
        """测试被邀请人回复后，被邀请人进行remove"""
        res = share_remove_jenny_reply(shareId)
        self.assertIn('"code":0', res.text)

    def test_invite_remove_05(self):
        """测试remove的id错误或不存在"""
        res = share_remove(share_id + "1")
        self.assertIn('"code":2202', res.text)

    def test_invite_remove_06(self):
        """测试remove的id为空"""
        res = share_remove("")
        self.assertIn('"code":302', res.text)


if __name__ == '__main__':
    unittest.main()
