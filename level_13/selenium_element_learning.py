# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     selenium_element_learning
   Description :  
   Author :       kirk
   date：          2022/5/7
-------------------------------------------------
   Change Activity:
                   2022/5/7
-------------------------------------------------
"""
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com")  # 打开B站主页

# id定位
"""
print(driver.find_element('id', 'i_cecream'))  # 定位id为i_cecream的元素
"""

# name定位
"""
print(driver.find_element('name', 'keywords'))  # 定位name为keywords的元素
"""

# # class name定位
"""
print(driver.find_element('class name', 'old-browser-tip'))  # 定位class属性为old-browser-tip的元素
# 对于复合样式(例如:bili-header large-header)不能直接使用class name来进行定位
print(driver.find_element('class name', 'bili-header large-header'))    # 会报错
"""

# tag name定位: 一般用于查找同类元素
"""
print(len(driver.find_elements('tag name', 'input')))  # 定位tag name属性为input的元素
"""

# link text定位(属性值精准定位):用于定位超链接a标签
"""
driver.find_element('link text', '番剧').click()  # 点击link text属性为番剧的超链接
"""

# partial link text定位(属性值可以为部分)：用于定位超链接a标签
"""
driver.find_element('partial link text', '直').click()   # 点击link text属性包含直这个字的超链接
"""

# xpath定位
"""
# 绝对路径定位法
print(driver.find_element('xpath', '/html/body/div'))   # 定位绝对路径为/html/body/div的元素

# 相对路径定位法
driver.find_element('xpath', '//body/div[2]//li[2]').click()    # 点击番剧的相对路径

# xpath属性定位法
driver.find_element('xpath', '//div[@class="header-login-entry"]').click()
# 定位div标签class属性为header-login-entry的元素并点击
time.sleep(2)
# 定位input标签属性type值为text，placeholder属性值为请输入账号的元素并点击
driver.find_element('xpath', '//input[@type="text"][@placeholder="请输入账号"]').click()
# 定位placeholder属性值为请输入账号的元素并清空
driver.find_element('xpath', '//*[@placeholder="请输入账号"]').clear()
# 定位placeholder属性值为请输入账号的元素并输入12345678900
driver.find_element('xpath', '//*[@placeholder="请输入账号"]').send_keys("12345678900")

# xpath属性模糊定位
time.sleep(2)
# 定位属性中的text包含密码的元素并点击
driver.find_element('xpath', '//*[contains(text(),"密码")]').click()
# 定位input标签中属性包含placeholder并且值为请输入密码的元素并清空
driver.find_element('xpath', '//input[contains(@placeholder,"请输入密码")]').clear()
# 定位input标签中属性包含placeholder并且值为请输入密码的元素并输入123456
driver.find_element('xpath', '//input[contains(@placeholder,"请输入密码")]').send_keys('123456')

time.sleep(2)
# 定位属性class值为bili-mini-login-register-wrapper的目录下的第二个子级div标签并点击
driver.find_element('xpath', '//*[@class="bili-mini-login-register-wrapper"]/div[2]').click()
"""

# css selector定位
"""
# 利用元素标签来定位所有相同元素
div = driver.find_elements('css selector', 'div')   # 定位标签为div的元素，返回列表
print(len(div))

# 利用class属性来进行定位(css样式需要加.作为开头)
driver.find_element('css selector', '.banner-link').click()     # 定位class属性为banner-link的元素并点击
# 定位class属性为right-entry__outside go-login-btn的复合css样式并点击
driver.find_element('css selector', '.right-entry__outside.go-login-btn').click()

# 利用id属性来进行定位(用#号表示id属性后跟id属性值)
print(driver.find_element('css selector', '#i_cecream'))

# 多属性定位
# 定位target属性为_blank，class属性为default-entry的第一个元素并点击
driver.find_elements('css selector', "[target='_blank'][class='default-entry']")[0].click()

# 利用父子位置关系来定位(父子关系 > 号连接)
print(driver.find_element('css selector', 'body > iframe').tag_name)
driver.find_element('css selector',
                    'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) '
                    '> ul:nth-child(3) > li:nth-child(1) > li > div > div').click()
# 注意nth-child()的序号，从1开始，其他的标签也要计数，例如body下第4个标签是要进入的div子级，但是只数div可能是第2个，这里需要填写的序号应该为4

# 组合定位，先用id定位父级，再用class属性定位子级，无法定位的再考虑位置定位
driver.find_element('css selector',
                    '#i_cecream > div.bili-header.large-header > div.bili-header__bar '
                    '> ul.right-entry > li:nth-child(1) > li > div > div').click()


# 利用孙子位置关系来定位(孙子关系 空格连接)
driver.find_element('css selector', 'ul.right-entry div.header-login-entry').click()

# 模糊匹配，相当于xpath中的contains
driver.find_element('css selector', 'div[class*="header-login-entry"]').click()
"""

# 退出进程
time.sleep(5)
driver.quit()
