import unittest
from modules.user_manage.user_info.user_avatar_upload import *

with open(r"C:\AIOT\test.jpg", encoding='utf-8') as f:
    avatar_file = f.read()


class TestAvatarUpload(unittest.TestCase):
    """
    上传用户头像(或更改用户头像)
    """
    @unittest.skip("该接口暂时没搞定")
    def test_avatar_upload_01(self):
        """上传用户头像(或更改用户头像)"""
        result = avatar_upload(avatar_file)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
