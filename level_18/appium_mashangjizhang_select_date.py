# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     appium_laogejizhang_select_date
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


def select_date(year: int, month: int):
    # 设置year
    while True:
        current_year = \
            driver.find_element("xpath", "//android.widget.TextView[@bounds='[506,2381][776,2449]']").text
        if current_year == str(year):
            print("年份调对勒")
            break
        elif int(current_year) < year:
            print("年份小了，往下调")
            driver.swipe(650, 2400, 650, 2320)
            time.sleep(1)
        else:
            print("年份大了，往上调")
            driver.swipe(650, 2320, 650, 2400)
            time.sleep(1)

    # 设置month
    while True:
        current_month = driver.find_element("xpath", "//android.widget.TextView[@bounds='[844,2381][1114,2449]']").text
        if current_month == str(month):
            print("月份调对勒")
            break
        elif int(current_month) < month:
            print("月份小了，往下调")
            driver.swipe(980, 2400, 980, 2320)
            time.sleep(1)
        else:
            print("月份大了，往上调")
            driver.swipe(980, 2320, 980, 2400)
            time.sleep(1)

    driver.find_element("xpath", "//android.widget.TextView[@text='确定']").click()
    print("日期调整完成")


desired_cap = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "appPackage": "com.laogejizhang.account",
    "appActivity": ".MainActivity",
    "automationName": "Uiautomator2",
    "noReset": True,
    "newCommandTimeout": 6000,
    "unicodeKeyboard": True,
    "resetKeyboard": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(20)

driver.find_element("xpath", "//android.widget.TextView[@text='流水']").click()
time.sleep(1)
driver.find_element("xpath", "//android.widget.TextView[@bounds='[621,102][935,180]']").click()
time.sleep(1)
select_date(2021, 4)
