import unittest
from modules.res_manage.res_history_delete.res_history_delete import *
from config import readcfg

subjectId_Gary = readcfg.subjectId_Gary_hub
subjectId_Jenny = readcfg.subjectId_Jenny


class TestResHistoryDelete(unittest.TestCase):
    """
    删除历史记录
    """

    def test_res_history_delete_01(self):
        """测试删除历史记录"""
        result = res_history_delete(subjectId_Gary)
        self.assertIn('"code":0', result.text)

    def test_res_history_delete_02(self):
        """测试id错误或不存在"""
        result = res_history_delete(subjectId_Gary.replace("0", "1"))
        self.assertIn('"code":706', result.text)

    def test_res_history_delete_03(self):
        """测试查询其他人的设备id"""
        result = res_history_delete(subjectId_Jenny)
        self.assertIn('"code":706', result.text)

    def test_res_history_delete_04(self):
        """测试查询设备id为空"""
        result = res_history_delete("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
