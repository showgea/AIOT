import unittest
from modules.ifttt_manage.ifttt_config.ifttt_subject_action_query import *
from config import readcfg

subjectModel = readcfg.subjectModel
subjectId_Gary_hub = readcfg.subjectId_Gary_hub


class TestIftttSubjectTriggerQuery(unittest.TestCase):
    """
    查询指定的应用类型下有哪些Action（Then）
    """

    def test_ifttt_subject_action_query_01(self):
        """测试查询指定的应用类型下有哪些Action"""
        result = ifttt_subject_action_query(subjectModel, subjectId_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_ifttt_subject_action_query_02(self):
        """测试subjectModel错误或不存在"""
        result = ifttt_subject_action_query(subjectModel + "1", subjectId_Gary_hub)
        self.assertIn('"code":0', result.text)

    def test_ifttt_subject_action_query_04(self):
        """测试subjectModel为空"""
        result = ifttt_subject_action_query("", subjectId_Gary_hub)
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
