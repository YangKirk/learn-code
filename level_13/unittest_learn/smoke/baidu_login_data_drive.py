# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     baidu_login_data_drive
   Description :  
   Author :       kirk
   date：          2022/5/18
-------------------------------------------------
   Change Activity:
                   2022/5/18
-------------------------------------------------
"""
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ddt import ddt, data, unpack
from level_13.unittest_learn.smoke.util import Util
import unittest


@ddt  # 一定要在类名前加ddt装饰器
class BaiduLoginTest(unittest.TestCase):

    def setUp(self) -> None:

        self.driver = webdriver.Chrome()
        self.url = 'https://www.baidu.com'
        self.driver.implicitly_wait(20)
        self.imgs = []  # 用于保存截图

    def tearDown(self) -> None:
        self.driver.quit()

    def find_element(self, locator: tuple):
        try:
            element = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(*locator))
            return element
        except NoSuchElementException as e:
            print('Error details: {}'.format(e.args[0]))
            raise e

    def test_login_success(self):
        """
        测试当用户名和密码正确时，用户能够成功登陆到系统中
        :return:
        """
        self.driver.get(self.url)
        self.find_element(('id', 's-top-loginbtn')).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(('id', 'TANGRAM__PSP_11__userName')))
        self.find_element(('id', 'TANGRAM__PSP_11__userName')).clear()
        self.find_element(('id', 'TANGRAM__PSP_11__userName')).send_keys(Util.username)
        time.sleep(1)
        self.find_element(('id', 'TANGRAM__PSP_11__password')).clear()
        self.find_element(('id', 'TANGRAM__PSP_11__password')).send_keys(Util.password)
        time.sleep(1)
        self.find_element(('id', 'TANGRAM__PSP_11__submit')).click()
        WebDriverWait(self.driver, 30).until(
            ec.text_to_be_present_in_element(('css selector', '.user-name.c-font-normal.c-color-t'), Util.username))
        login_name = self.find_element(('css selector', '.user-name.c-font-normal.c-color-t')).text
        self.imgs.append(self.driver.get_screenshot_as_base64())  # 执行截图操作，将当前截图加入到测试报告中
        self.assertEqual(login_name, Util.username)

    @data(
        *Util.get_data()  # 通过函数调用获取数据，数据需要解包传入
    )
    # 通过读取文件获取数据，数据需要解包传入
    # @data(
    #     *Util.get_data_from_file('/home/kirk/Desktop/learn-code/level_13/unittest_learn/smoke/data.txt')
    # )
    @unpack
    def stest_dataTest_login_failed(self, username, password, err):
        """
        通过数据驱动测试所有登陆失败的测试用例
        :return:
        """
        self.driver.get(self.url)
        time.sleep(1)
        self.find_element(('id', 's-top-loginbtn')).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(('id', 'TANGRAM__PSP_11__userName')))
        self.find_element(('id', 'TANGRAM__PSP_11__userName')).clear()
        self.find_element(('id', 'TANGRAM__PSP_11__userName')).send_keys(username)
        time.sleep(1)
        self.find_element(('id', 'TANGRAM__PSP_11__password')).clear()
        self.find_element(('id', 'TANGRAM__PSP_11__password')).send_keys(password)
        time.sleep(1)
        self.find_element(('id', 'TANGRAM__PSP_11__submit')).click()
        login_msg = self.find_element(('id', 'TANGRAM__PSP_11__error')).text
        if login_msg == '':
            login_msg = self.find_element(('xpath', "//*[contains(text(),'，请重新输入或')]")).text
        self.imgs.append(self.driver.get_screenshot_as_base64())  # 执行截图操作，将当前截图加入到测试报告中
        self.assertEqual(login_msg, err)
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
