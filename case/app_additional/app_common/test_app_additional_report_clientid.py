import unittest
from modules.app_additional.app_common.app_additional_report_clientid import *


class TestAppAdditionalReportClientId(unittest.TestCase):
    """
    APP上传clientId,有效时间10分钟
    """

    def test_app_additional_report_clientid_01(self):
        """测试APP上传clientId,有效时间10分钟"""
        result = app_additional_report_clientid("123")
        self.assertIn('"code":0', result.text)


if __name__ == '__main__':
    unittest.main()
