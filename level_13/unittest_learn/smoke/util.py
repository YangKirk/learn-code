# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     util
   Description :  
   Author :       kirk
   date：          2022/5/18
-------------------------------------------------
   Change Activity:
                   2022/5/18
-------------------------------------------------
"""
import json
import os
import sys

if getattr(sys, 'frozen', False):
    current_path = os.path.dirname(sys.executable)
else:
    current_path = os.path.dirname(os.path.realpath(__file__))

config_json_file_path = os.path.join(current_path, 'smoke_test_baidu_login.json')

if os.path.isfile(config_json_file_path):
    with open(config_json_file_path, 'r',
              encoding='utf-8') as data:
        conf = json.load(data)


class Util:
    username = conf.get("username")
    password = conf.get("password")

    @classmethod
    def get_data(cls):
        """
        通过此函数返回数据
        :return:
        """
        testdata = [
            ("", cls.password, '请您输入手机号/用户名/邮箱'),
            (cls.username, "", "请您输入密码"),
            (cls.username + 'x', cls.password, '用户名或密码有误，请重新输入或找回密码'),
            (cls.username, cls.password + 'x', '用户名或密码有误，请重新输入或找回密码')
        ]
        return testdata

    @classmethod
    def get_data_from_file(cls, path):
        """
        通过文件获取数据
        :param path: 文件路径
        :return:
        """
        rows = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                user_data = line.strip().split(',')
                rows.append(user_data)
        return rows
