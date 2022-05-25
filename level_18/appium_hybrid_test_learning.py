# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     appium_hybrid_test_learning
   Description :
   Author :       Kirk
   date：          2022/5/25
-------------------------------------------------
   Change Activity:
                   2022/5/25:
-------------------------------------------------
"""
from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.android.browser",
    "appActivity": ".BrowserActivity",
    "automationName": "Uiautomator2",
    "noReset": True,
    "newCommandTimeout": 6000,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
}

# 这个路径地址给的是本机的4723端口，默认是appium服务器的端口
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)  # 隐式等待

# 点击网址栏->清空输入拼多多网址->点击回车键
driver.find_element("id", "com.android.browser:id/url").click()
driver.find_element("id", "com.android.browser:id/url").clear()
driver.find_element("id", "com.android.browser:id/url").send_keys("http://mobile.yangkeduo.com")
driver.press_keycode(66)  # 回车事件

context = driver.contexts  # 获取当前app中的上下文对象(类似切换iframe，从手机端切换到网页端)
print(context)  # 打印当前页面中的context

driver.switch_to.context("WEBVIEW_com.android.browser")  # 传入H5端页面的context进行切换
driver.find_element("xpath", "//span[text()='女装']").click()
