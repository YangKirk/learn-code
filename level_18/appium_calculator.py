# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     appium_calculator
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

desired_cap = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.kxwnqjsq.lusem",
    "appActivity": "com.example.calculator.control.main_nav",
    "automationName": "Uiautomator2",
    "newCommandTimeout": 6000,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)

# 打开计算器
dic = [
    {'num1': 78, "num2": 98, "op": '+'},
    {'num1': 56, "num2": 34, "op": '-'},
    {'num1': 34, "num2": 2, "op": '*'},
    {'num1': 123, "num2": 89, "op": '/'},
]

number_dic = {
    "0": "spn2",
    "1": "dum1",
    "2": "zbmz",
    "3": "bzmv",
    "4": "btlh",
    "5": "zvlg",
    "6": "kamr",
    "7": "gnmq",
    "8": "dtl_",
    "9": "pwm0",
}

op_dic = {
    "+": "fnmd",
    "-": "rkms",
    "*": "rolv",
    "/": "knlf"
}

for exp in dic:

    # 解析第一个操作数, 将数字转换为字符串再切分后依次点击
    for word in str(exp['num1']):
        driver.find_element("id", "com.kxwnqjsq.lusem:id/{}".format(number_dic[word])).click()

    time.sleep(1)
    # 解析操作符
    driver.find_element("id", f"com.kxwnqjsq.lusem:id/{op_dic[exp['op']]}").click()

    time.sleep(1)

    # 解析第二个操作数, 将数字转换为字符串再切分后依次点击
    for word in str(exp["num2"]):
        driver.find_element("id", "com.kxwnqjsq.lusem:id/{}".format(number_dic[word])).click()

    time.sleep(1)

    # 点击等号
    driver.find_element("id", "com.kxwnqjsq.lusem:id/yvle").click()

    time.sleep(1)

    # 打印结果
    print(driver.find_element("id", "com.kxwnqjsq.lusem:id/iflq").text)
