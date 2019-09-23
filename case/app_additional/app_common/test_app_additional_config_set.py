import unittest
from modules.app_additional.app_common.app_additional_config_set import *


class TestAppAdditionalConfigSet(unittest.TestCase):
    """
    通用接口(设置配置项)
    """

    def test_app_additional_config_set_01(self):
        """测试通用接口(设置配置项)"""
        result = app_additional_config_set("xxx", "xxx", "xxx")
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
