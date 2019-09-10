import unittest
from modules.service_manage.service_related.service_write import *
from config import readcfg

serviceId_cube = readcfg.serviceId_cube
serviceId_wrong = readcfg.serviceId_wrong
data = {"cube_status": "shake_air"}


class TestServiceWrite(unittest.TestCase):
    """
    提交service控制指令
    """

    def test_service_write_01(self):
        """测试提交service控制指令"""
        result = service_write(serviceId_cube, data)
        self.assertIn('"code":0', result.text)

    def test_service_write_02(self):
        """测试serviceId错误或不存在"""
        result = service_write(serviceId_wrong, data)
        self.assertIn('"code":709', result.text)

    def test_service_write_06(self):
        """测试serviceId为空"""
        result = service_write("", data)
        self.assertIn('"code":302', result.text)

    def test_service_write_07(self):
        """测试data为空"""
        result = service_write(serviceId_cube, data={})
        self.assertIn('"code":302', result.text)


if __name__ == '__main__':
    unittest.main()
