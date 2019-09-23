import unittest
from modules.app_additional.app_common.app_additional_config_delete import *


class TestAppAdditionalConfigDelete(unittest.TestCase):
    """
    通用接口(删除配置项)
    """

    def test_app_additional_config_delete_01(self):
        """测试通用接口(删除配置项)"""
        result = app_additional_config_delete("xxx")
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
