import unittest
from modules.positon_manage.position_based_query.position_subjectModel_query import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
size = 10
startIndex = 0


class TestPositionSubjectModelQuery(unittest.TestCase):
    """
    查询某个位置下subjectModel类型
    """

    def test_position_subjectModel_query_01(self):
        """测试查询用户自己的家下面的subjectModel类型"""
        result = position_subjectModel_query(positionId_Gary, size, startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_subjectModel_query_02(self):
        """测试查询位置错误或不存在"""
        result = position_subjectModel_query(positionId_Gary.replace("2", "3"), size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_position_subjectModel_query_03(self):
        """测试查询其他用户下位置"""
        result = position_subjectModel_query(positionId_Jenny, size, startIndex)
        self.assertIn('"code":710', result.text)

    def test_position_subjectModel_query_04(self):
        """测试请求参数size为0"""
        result = position_subjectModel_query(positionId_Gary, size=0, startIndex=startIndex)
        self.assertIn('"code":302', result.text)

    def test_position_subjectModel_query_05(self):
        """测试请求参数size为1"""
        result = position_subjectModel_query(positionId_Gary, size=1, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_subjectModel_query_06(self):
        """测试请求参数不传size"""
        result = position_subjectModel_query(positionId_Gary, size=None, startIndex=startIndex)
        self.assertIn('"code":0', result.text)

    def test_position_subjectModel_query_07(self):
        """测试请求参数不传startIndex"""
        result = position_subjectModel_query(positionId_Gary, size, startIndex=None)
        self.assertIn('"code":0', result.text)

    def test_position_subjectModel_query_08(self):
        """测试请求参数不传size和startIndex"""
        result = position_subjectModel_query(positionId_Gary, size=None, startIndex=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
