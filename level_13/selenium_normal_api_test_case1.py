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
import time

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
driver.get("https://www.baidu.com")

driver.set_window_size(200, 500)  # 设置窗口大小为宽200,高500
time.sleep(5)  # 等待5秒
driver.maximize_window()  # 最大化窗口
time.sleep(5)
driver.refresh()  # 刷新窗口

print(driver.page_source)  # 打印源码

# 找到搜索框，输入深空之眼进行搜索
driver.find_element('id', 'kw').click()  # 定位到属性id值为kw的元素并点击它
driver.find_element('id', 'kw').clear()  # 定位到属性id值为kw的元素并清空里面的内容
driver.find_element('id', 'kw').send_keys("深空之眼")  # 定位到id为kw的元素并输入深空之眼
driver.find_element('id', 'su').click()  # 定位到属性id值为su的元素并点击它

print(driver.name)  # 打印窗口名
print(driver.title)  # 打印页面标题
print(driver.current_url)  # 打印当前窗口地址
driver.get_screenshot_as_file('selenium_learning_img.png')

# 等待10秒关闭浏览器
time.sleep(10)
driver.quit()  # 关闭进程
# driver.close()  # 关闭当前窗口
