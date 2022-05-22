# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     appium_start_setting_learning
   Description :  
   Author :       kirk
   date：          2022/5/22
-------------------------------------------------
   Change Activity:
                   2022/5/22
-------------------------------------------------
"""
import time

from appium import webdriver

desired_cap = {}

# 必须参数，定义被测脚本的平台属性，不区分大小写，但必须是android/ios
desired_cap['platformName'] = 'Android'

# 必须参数,定义被测手机的安卓版本号/ios版本，(设置->关于本机->android版本/ios版本，必须跟被测机对的上,不能乱写，大版本不能错，小版本可以不用写)
desired_cap['platformVersion'] = '6.0.1'

# 可以写任意的值，但是不能为空
desired_cap['deviceName'] = '127.0.0.1:7555'

# 必须参数，指定被测软件的包名
desired_cap['appPackage'] = 'com.android.settings'

# 必须参数，指定要打开的app的页面是哪个
desired_cap['appActivity'] = '.Settings'

# 不是必须的，但是一般需要指定Uiautomator2
desired_cap['automationName'] = 'Uiautomator2'

# 设置app的重置策略，可选参数值为默认/fullReset/noReset
# 默认: 测试后停止并清除应用数据，不卸载APP
# fullReset:在会话开始前 测试后停止app，清除app数据并卸载app
# noReset：不要停止应用程序，不要清除应用数据，不要卸载app
desired_cap['noReset'] = True

# 设置命令的超时时间
desired_cap['newCommandTimeout'] = 6000

# 用于设置中文输入
desired_cap['unicodeKeyboard'] = True
desired_cap['resetKeyboard'] = True

# 初始化
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

driver.find_element('id', 'com.ibox.calculators:id/digit4').click()
driver.find_element('id', 'com.ibox.calculators:id/plus').click()
driver.find_element('id', 'com.ibox.calculators:id/digit5').click()
driver.find_element('id', 'com.ibox.calculators:id/equal').click()
# driver.find_element('xpath','//*[@text="="]').click()
time.sleep(1)
print(driver.find_element('xpath', '//android.widget.TextView[@bounds="[40,105][706,203]"]').text)
