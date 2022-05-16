# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     smoke_test_bilibili_login
   Description :  
   Author :       kirk
   date：          2022/5/16
-------------------------------------------------
   Change Activity:
                   2022/5/16
-------------------------------------------------
"""
import json
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import unittest

if getattr(sys, 'frozen', False):
    current_path = os.path.dirname(sys.executable)
else:
    current_path = os.path.dirname(os.path.realpath(__file__))

config_json_file_path = os.path.join(current_path, 'smoke_test_baidu_login.json')


class BaiduLoginTest(unittest.TestCase):

    def setUp(self) -> None:
        if os.path.isfile(config_json_file_path):
            with open(config_json_file_path, 'r',
                      encoding='utf-8') as data:
                conf = json.load(data)
        self.username = conf.get("username")
        self.password = conf.get("password")
        self.driver = webdriver.Chrome()
        self.url = 'https://www.baidu.com'
        self.driver.implicitly_wait(20)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_success(self):
        """
        测试当用户名和密码正确时，用户能够成功登陆到系统中
        :return:
        """
        self.driver.get(self.url)
        self.driver.find_element('id', 's-top-loginbtn').click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(('id', 'TANGRAM__PSP_11__userName')))
        self.driver.find_element('id', 'TANGRAM__PSP_11__userName').clear()
        self.driver.find_element('id', 'TANGRAM__PSP_11__userName').send_keys(self.username)
        time.sleep(1)
        self.driver.find_element('id', 'TANGRAM__PSP_11__password').clear()
        self.driver.find_element('id', 'TANGRAM__PSP_11__password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element('id', 'TANGRAM__PSP_11__submit').click()
        WebDriverWait(self.driver, 30).until(
            ec.text_to_be_present_in_element(('css selector', '.user-name.c-font-normal.c-color-t'), self.username))
        login_name = self.driver.find_element('css selector', '.user-name.c-font-normal.c-color-t').text
        self.assertEqual(login_name, self.username)

    def test_login_failed_without_username(self):
        """
        测试没有输入用户名时，登陆失败的情况
        :return:
        """
        self.driver.get(self.url)
        self.driver.find_element('id', 's-top-loginbtn').click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(('id', 'TANGRAM__PSP_11__userName')))
        self.driver.find_element('id', 'TANGRAM__PSP_11__userName').clear()
        self.driver.find_element('id', 'TANGRAM__PSP_11__userName').send_keys('')
        time.sleep(1)
        self.driver.find_element('id', 'TANGRAM__PSP_11__password').clear()
        self.driver.find_element('id', 'TANGRAM__PSP_11__password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element('id', 'TANGRAM__PSP_11__submit').click()
        login_msg = self.driver.find_element('id', 'TANGRAM__PSP_11__error').text
        self.assertEqual(login_msg, '请您输入手机号/用户名/邮箱')
        time.sleep(1)

    def test_login_failed_without_password(self):
        """
        测试没有输入密码时，登陆失败的情况
        :return:
        """
        self.driver.get(self.url)
        self.driver.find_element('id', 's-top-loginbtn').click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(('id', 'TANGRAM__PSP_11__userName')))
        self.driver.find_element('id', 'TANGRAM__PSP_11__userName').clear()
        self.driver.find_element('id', 'TANGRAM__PSP_11__userName').send_keys(self.username)
        time.sleep(1)
        self.driver.find_element('id', 'TANGRAM__PSP_11__password').clear()
        self.driver.find_element('id', 'TANGRAM__PSP_11__password').send_keys('')
        time.sleep(1)
        self.driver.find_element('id', 'TANGRAM__PSP_11__submit').click()
        login_msg = self.driver.find_element('id', 'TANGRAM__PSP_11__error').text
        self.assertEqual(login_msg, '请您输入密码')
        time.sleep(1)

    def test_login_failed_with_error_username(self):
        """
        测试输入错误用户名时，登陆失败的情况
        :return:
        """
        self.driver.get(self.url)
        self.driver.find_element('id', 's-top-loginbtn').click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(('id', 'TANGRAM__PSP_11__userName')))
        self.driver.find_element('id', 'TANGRAM__PSP_11__userName').clear()
        self.driver.find_element('id', 'TANGRAM__PSP_11__userName').send_keys(self.username + 'x')
        time.sleep(1)
        self.driver.find_element('id', 'TANGRAM__PSP_11__password').clear()
        self.driver.find_element('id', 'TANGRAM__PSP_11__password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element('id', 'TANGRAM__PSP_11__submit').click()
        login_msg = self.driver.find_element('xpath', '//*[contains(text(),"用户名或密码有误，请重新输入或")]').text
        self.assertEqual(login_msg, '用户名或密码有误，请重新输入或找回密码')
        time.sleep(1)

    def test_login_failed_with_error_password(self):
        """
        测试输入错误密码时，登陆失败的情况
        :return:
        """
        self.driver.get(self.url)
        self.driver.find_element('id', 's-top-loginbtn').click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(('id', 'TANGRAM__PSP_11__userName')))
        self.driver.find_element('id', 'TANGRAM__PSP_11__userName').clear()
        self.driver.find_element('id', 'TANGRAM__PSP_11__userName').send_keys(self.username)
        time.sleep(1)
        self.driver.find_element('id', 'TANGRAM__PSP_11__password').clear()
        self.driver.find_element('id', 'TANGRAM__PSP_11__password').send_keys(self.password + 'x')
        time.sleep(1)
        self.driver.find_element('id', 'TANGRAM__PSP_11__submit').click()
        login_msg = self.driver.find_element('xpath', '//*[contains(text(),"用户名或密码有误，请重新输入或")]').text
        self.assertEqual(login_msg, '用户名或密码有误，请重新输入或找回密码')
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
