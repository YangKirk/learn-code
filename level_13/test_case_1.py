# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_case_1
   Description :  
   Author :       kirk
   date：          2022/2/11
-------------------------------------------------
   Change Activity:
                   2022/2/11
-------------------------------------------------
"""
from selenium import webdriver

"""
安装与配置selenium环境
1.直接用pip install selenium
在调用chromedriver的会出现
Message: ‘chromedriver’ executable needs to be in PATH
2.需要配置环境变量，分Windows和linux
linux配置: 去http://chromedriver.storage.googleapis.com/index.html下载对应版本的chrome驱动
3.解压驱动得到chromedriver文件
打开终端输入: sudo chmod 777 chromedirver -> sudo cp chromedriver /usr/bin(路径需要填写正确)
环境变量配置成功
"""

"""selenium test case 1"""
# 打开浏览器
driver = webdriver.Chrome()

# 加载第一个网页
driver.get("https://www.bilibili.com")
