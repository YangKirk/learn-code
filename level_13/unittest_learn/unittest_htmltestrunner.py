# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     unittest_htmltestrunner
   Description :  
   Author :       kirk
   date：          2022/5/17
-------------------------------------------------
   Change Activity:
                   2022/5/17
-------------------------------------------------
"""
from level_13.unittest_learn.smoke.baidu_login_data_drive import BaiduLoginTest
from HTMLTestRunnerCN import HTMLTestReportCN
import unittest

if __name__ == '__main__':
    """测试前请去smoke文件中填写json文件参数或data.txt文件参数"""
    test1 = unittest.defaultTestLoader.loadTestsFromTestCase(BaiduLoginTest)
    suite = unittest.TestSuite(test1)

    runner = HTMLTestReportCN(
        title='带截图的百度登陆测试报告',
        description='xxx软件测试报告v0.1',
        stream=open('sample_test_report.html', 'wb'),
        verbosity=2,
        tester='Kirk'
    )
    runner.run(suite)
