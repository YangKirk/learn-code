# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     unittest_assert_fail_screenshot
   Description :  
   Author :       kirk
   date：          2022/5/18
-------------------------------------------------
   Change Activity:
                   2022/5/18
-------------------------------------------------
"""
import os
import time
from selenium import webdriver
import unittest


# 定义截图装饰器
def add_pic(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except AssertionError as e:
            day = time.strftime('%Y%m%d', time.localtime(time.time()))
            screenshot_path = os.getcwd() + r'\reports\screenshot_%s' % day
            if not os.path.exists(screenshot_path):
                os.makedirs(screenshot_path)

            tm = time.strftime('%H%M%S', time.localtime(time.time()))
            y = lambda x: x.get_screenshot_as_file(screenshot_path + '/{}_{}.png'.format('screen_shot', tm))
            print(y)
            raise e

    return wrapper


class AssertTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com"

    def tearDown(self) -> None:
        self.driver.quit()

    def test_demo1(self):
        try:
            self.driver.get(self.url)
            self.assertEqual(1, 2)
        except AssertionError as e:
            day = time.strftime('%Y%m%d', time.localtime(time.time()))  # 捕捉年月日
            # 截图存放路径
            screenshot_path = os.getcwd() + r'\reports\screenchot_%s' % day  # 通过os.getcwd()获取当前绝对路径
            if not os.path.exists(screenshot_path):
                os.makedirs(screenshot_path)

            tm = time.strftime('%H%M%S', time.localtime(time.time()))  # 捕捉时分秒
            self.driver.get_screenshot_as_file(screenshot_path + r'/{}_{}.png'.format('screen_shot', tm))
            raise e  # 继续抛出异常给unittest，必须写

    @add_pic
    def testFunc(self):
        self.driver.get(self.url)
        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()
