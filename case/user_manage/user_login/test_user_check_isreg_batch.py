import unittest
from modules.user_manage.user_login.user_check_isreg_batch import *

accountList = [
    {
      "account": "yuzhen.peng@aqara.com"
    },
    {
      "account": "guobing.tang@aqara.com"
    },
    {
      "account": "18682246872"
    },
    {
        "account": "13798371392"
    }
  ]


class TestUserCheckIsregBatch(unittest.TestCase):
    """批量检查账户是否已注册"""

    def test_user_check_isreg_batch_01(self):
        """测试批量检查账户是否已注册"""
        result = user_check_isreg_batch(accountList)
        isreg = json.loads(result.text)["result"][0]["isreg"]
        self.assertEqual(1, isreg)

    def test_user_check_isreg_batch_02(self):
        """测试检查的账户错误或不存在"""
        result = user_check_isreg_batch(accountList)
        isreg = json.loads(result.text)["result"][3]["isreg"]
        self.assertEqual(0, isreg)

    def test_user_check_isreg_batch_03(self):
        """测试检查账户为空"""
        result = user_check_isreg_batch([])
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
