import unittest
from modules.positon_manage.position_based_query.position_service_query import *
from config import readcfg

positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
positionId_wrong = readcfg.positionId_wrong
serviceTypes = ["S_SENSOR_CUBE", "S_SENSOR_PRESSURE", "S_SENSOR_TEMPERATURE", "S_SENSOR_HUMIDITY", "S_CORRIDOR_LIGHT"]
subjectModels = ["lumi.gateway.aqhm01", "lumi.weather.v1", "lumi.sensor_cube.aqgl01"]
access = "rw"
size = readcfg.size
startIndex = readcfg.startIndex


class TestPositionServiceQuery(unittest.TestCase):
    """
    根据位置或serviceType查询service
    """
    def test_position_service_query_01(self):
        """测试查询用户自己的家下面的service"""
        result = position_service_query(positionId_Gary, serviceTypes, size, startIndex, subjectModels,
                                        labels=None, access=access)
        self.assertIn('"code":0', result.text)

    def test_position_service_query_02(self):
        """测试查询位置错误或不存在"""
        result = position_service_query(positionId_wrong, serviceTypes, size, startIndex, subjectModels,
                                        labels=None, access=access)
        self.assertIn('"code":710', result.text)

    def test_position_service_query_03(self):
        """测试查询其他用户下位置"""
        result = position_service_query(positionId_Jenny, serviceTypes, size, startIndex, subjectModels,
                                        labels=None, access=access)
        self.assertIn('"code":710', result.text)

    def test_position_service_query_04(self):
        """测试请求参数size为0"""
        result = position_service_query(positionId_Gary, serviceTypes, size=0, startIndex=startIndex,
                                        subjectModels=subjectModels, labels=None, access=access)
        self.assertIn('"code":302', result.text)

    def test_position_service_query_05(self):
        """测试请求参数size为1"""
        result = position_service_query(positionId_Gary, serviceTypes, size=1, startIndex=startIndex,
                                        subjectModels=subjectModels, labels=None, access=access)
        self.assertIn('"code":0', result.text)

    def test_position_service_query_06(self):
        """测试请求参数不传size"""
        result = position_service_query(positionId_Gary, serviceTypes, size=None, startIndex=startIndex,
                                        subjectModels=subjectModels, labels=None, access=access)
        self.assertIn('"code":0', result.text)

    def test_position_service_query_07(self):
        """测试请求参数不传startIndex"""
        result = position_service_query(positionId_Gary, serviceTypes, size, startIndex=None,
                                        subjectModels=subjectModels, labels=None, access=access)
        self.assertIn('"code":0', result.text)

    def test_position_service_query_08(self):
        """测试请求参数不传subjectModels"""
        result = position_service_query(positionId_Gary, serviceTypes, size, startIndex,
                                        subjectModels=None, labels=None, access=access)
        self.assertIn('"code":0', result.text)

    def test_position_service_query_09(self):
        """测试请求参数不传serviceTypes"""
        result = position_service_query(positionId_Gary, serviceTypes=None, size=size, startIndex=startIndex,
                                        subjectModels=subjectModels, labels=None, access=access)
        self.assertIn('"code":0', result.text)

    def test_position_service_query_10(self):
        """测试请求参数不传access"""
        result = position_service_query(positionId_Gary, serviceTypes=serviceTypes, size=size, startIndex=startIndex,
                                        subjectModels=subjectModels, labels=None, access=None)
        self.assertIn('"code":0', result.text)

    def test_position_service_query_11(self):
        """测试请求参数只传positionId"""
        result = position_service_query(positionId_Gary, serviceTypes=None, size=None, startIndex=None,
                                        subjectModels=None, labels=None, access=None)
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
