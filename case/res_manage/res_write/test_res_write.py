import unittest
from modules.res_manage.res_write.res_write import *
from config import readcfg

subjectId_Gary = readcfg.subjectId_Gary_hub
subjectId_Jenny = readcfg.subjectId_Jenny
data = {"corridor_light_status": 1, "brightness_level": 25}


class TestResWrite(unittest.TestCase):
    """
    提交控制指令
    """
    def test_res_write_01(self):
        """测试提交控制指令（网关开灯，亮度25）"""
        result = res_write(subjectId_Gary, data)
        self.assertIn('"code":0', result.text)

    def test_res_write_02(self):
        """测试id错误或不存在"""
        result = res_write(subjectId_Gary.replace("1", "2"), data)
        self.assertIn('"code":755', result.text)

    def test_res_write_03(self):
        """测试查询其他人的设备id"""
        result = res_write(subjectId_Jenny, data)
        self.assertIn('"code":755', result.text)

    def test_res_write_04(self):
        """测试设备id为空"""
        result = res_write("", data)
        self.assertIn('"code":302', result.text)

    def test_res_write_05(self):
        """测试设备资源列表为空"""
        result = res_write(subjectId_Gary, {})
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
