import unittest
from modules.user_manage.user_password.user_password_reset import *
from common.get_result_db import get_result_from_sql

# 123456
password = "e10adc3949ba59abbe56e057f20f883e"
# 654321
newPassword = "c33367701511b4f6020ec61ded352059"


class TestUserPasswordReset(unittest.TestCase):
    """
    用户修改密码
    """

    def test_user_password_reset_01(self):
        """输入原始密码不正确"""
        result = user_password_reset_wrong(newPassword + "1", newPassword)
        self.assertIn('"message":"密码错误"', result.text)

    def test_user_password_reset_02(self):
        """用户修改密码"""
        result = user_password_reset(password, newPassword)
        self.assertIn('"code":0', result.text)

    def test_user_password_reset_03(self):
        """输入原始密码为空"""
        result = user_password_reset("", newPassword)
        self.assertIn('"code":302', result.text)

    def test_user_password_reset_04(self):
        """输入新密码为空"""
        result = user_password_reset("", newPassword)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
