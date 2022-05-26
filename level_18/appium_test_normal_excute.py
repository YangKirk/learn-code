# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     appium_test_normal_excute
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
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType

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

# scroll滑动事件
"""
elm1 = driver.find_element("xpath", "//*[@text='应用']")
elm2 = driver.find_element("xpath", "//*[@text='蓝牙']")

driver.scroll(elm1, elm2, duration=10000)
"""

# drag_and_drop滑动事件
"""
elm1 = driver.find_element("xpath", "//*[@text='应用']")
elm2 = driver.find_element("xpath", "//*[@text='蓝牙']")

driver.drag_and_drop(elm1, elm2)
"""

# swipe滑动事件
"""
driver.swipe(500, 800, 500, 400, duration=1000)
"""

# tap轻敲手势事件
"""
elm1 = driver.find_element("xpath", "//*[@text='WLAN']")
ta = TouchAction(driver)    # 构造一个touch action对象
ta.tap(elm1).perform()  # 通过perform方法执行操作
ta.tap(x=600,y=500).perform()
"""

# long_press长按事件
driver.find_element('xpath', '//*[@text="WLAN"]').click()
ta = TouchAction(driver)
time.sleep(2)
ta.long_press(x=520, y=520).perform()

# press 按住事件/ move_to模拟手势移动操作事件
driver.start_activity('com.android.settings', '.ChooseLockPattern')  # 打开其他app或界面
ta = TouchAction(driver)
ta.press(x=260, y=1020).perform()  # 第一个点是press按住
ta.move_to(x=800, y=1020).perform()  # 后面的点是移动到目标坐标
ta.move_to(x=1350, y=1020).perform()
ta.move_to(x=1350, y=1550).perform()
ta.move_to(x=1350, y=2100).release().perform()  # 最后一个点通过release松手，再perform执行

print(driver.current_activity)  # 打印当前界面名
print(driver.current_package)  # 打印当前包名

# driver.close_app()  # 关闭当前app

# if driver.is_app_installed("com.mobivans.onestrokecharge"):  # 判断传入包名的APP是否已安装
#     print(driver.is_app_installed("com.mobivans.onestrokecharge"))  # 打印判断结果
#     driver.remove_app("com.mobivans.onestrokecharge")  # 卸载APP
# else:
#     print(driver.is_app_installed("com.mobivans.onestrokecharge"))  # 打印判断结果
#     driver.install_app(r"E:\apk\yibijizhang.apk")  # 安装APP
# time.sleep(1)

# driver.background_app(5)  # 将所有app置于后台,模拟home键操作

# print(driver.get_window_size())  # 获取当前手机或模拟器分辨率

# driver.get_screenshot_as_file(r"E:\apk\screen_shot.png")  # 手机截图
#
print(driver.network_connection)  # 打印当前手机网络状态
# driver.set_network_connection(ConnectionType.NO_CONNECTION)  # 设置手机网络状态为No connection
driver.set_network_connection(ConnectionType.AIRPLANE_MODE)  # 设置手机网络状态为Airplane mode
# driver.set_network_connection(ConnectionType.WIFI_ONLY)  # 设置手机网络状态为wifi only
# driver.set_network_connection(ConnectionType.DATA_ONLY)  # 设置手机网络状态为data only
# driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)  # 设置手机网络状态为All network on

# driver.press_keycode(66)    # 输入按键回车事件

driver.open_notifications()  # 打开手机通知栏

driver.quit()  # 退出driver对象
