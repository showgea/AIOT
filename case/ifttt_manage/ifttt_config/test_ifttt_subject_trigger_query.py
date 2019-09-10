import unittest
from modules.ifttt_manage.ifttt_config.ifttt_subject_trigger_query import *
from config import readcfg

subjectModel = readcfg.subjectModel


class TestIftttSubjectTriggerQuery(unittest.TestCase):
    """
    查询指定的应用类型下有哪些触发器（IF)
    """

    def test_ifttt_subject_trigger_query_01(self):
        """测试查询指定的应用类型下有哪些触发器"""
        result = ifttt_subject_trigger_query(subjectModel)
        self.assertIn('"code":0', result.text)

    def test_ifttt_subject_trigger_query_02(self):
        """测试subjectModel错误或不存在"""
        result = ifttt_subject_trigger_query(subjectModel + "1")
        self.assertIn('"code":0', result.text)

    def test_ifttt_subject_trigger_query_04(self):
        """测试subjectModel为空"""
        result = ifttt_subject_trigger_query("")
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
