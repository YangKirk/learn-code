# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     appium_open_kaifazhexuanxiang
   Description :
   Author :       Kirk
   date：          2022/5/26
-------------------------------------------------
   Change Activity:
                   2022/5/26:
-------------------------------------------------
"""
import time

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_cap = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "automationName": "Uiautomator2",
    "noReset": True,
    "newCommandTimeout": 6000,
    "unicodeKeyboard": True,
    "resetKeyboard": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)

while True:
    try:
        driver.find_element("xpath", "//*[@text='开发者选项']").click()
        print("找到了！")
        break
    except NoSuchElementException:
        print("当前页面没有发现开发者选项，往下滑动页面再次查找")
        driver.swipe(300, 500, 300, 300)
        time.sleep(1)
