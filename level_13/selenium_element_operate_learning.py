# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     selenium_element_operate_learning
   Description :  
   Author :       kirk
   date：          2022/5/10
-------------------------------------------------
   Change Activity:
                   2022/5/10
-------------------------------------------------
"""
import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.implicitly_wait(20)  # 隐式等待/全局等待:只会在元素未出现时生效，如果元素本身就存在则不会等待

# 常见元素操作
"""
driver.get("https://www.baidu.com")
driver.find_element('id', 'kw').click()     # 点击操作
driver.find_element('id', 'kw').clear()     # 清空文本框内容
driver.find_element('id', 'kw').send_keys('Python')     # 输入字符Python
print(driver.find_element('id', 'su').get_attribute("value"))  # 定位到属性id值为su的元素并获取此元素的value值
print(driver.find_element('link text', '贴吧').text)  # 定位到超链接text描述为贴吧的元素并打印此元素的text值
print(driver.find_element('id', 'form').is_displayed())  # 定位到属性id值为form的元素并判断此元素是否为隐藏，返回True or False
"""


# 显示等待
def func1():
    driver.get("https://www.baidu.com")
    WebDriverWait(driver, 10).until(ec.title_is("百度一下，你就知道"))  # 判断当前页面的title是否精确等于预期
    driver.find_element('id', 'kw').send_keys("正确")


# 显示等待
def func2():
    driver.get("https://www.baidu.com")
    WebDriverWait(driver, 5).until(ec.title_contains("百度一下"))  # 判断当前页面的title是否包含指定字符串
    driver.find_element('id', 'kw').send_keys("正确")


# 显示等待
def func3():
    driver.get("https://www.bilibili.com")
    WebDriverWait(driver, 5).until(ec.title_contains("哔哩哔哩"))  # 等待标题哔哩哔哩出现
    driver.execute_script("window.scrollTo(0,300);")  # 滑动页面滚轮从坐标0到300
    # 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(('class name', 'login-tip')))  # 判断悬浮登陆框是否出现
    driver.find_element('class name', 'login-tip').click()


# 显示等待
def func4():
    driver.get("http://www.baidu.com")
    # 判断某个元素是否可见,可见代表元素非隐藏，且元素的宽和高都不等于0，时间到了仍不可见报错
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(('link text', '高级搜索')))  # 需要以元组形式传入参数
    driver.find_element('link text', '高级搜索').click()


# 显示等待
def func5():
    driver.get("https://www.baidu.com")
    # 判断某个元素是否不可见,在等待时间内可见则报错
    WebDriverWait(driver, 10).until(ec.invisibility_of_element_located(('link text', '高级搜索')))  # 需要以元组形式传入参数


# 显示等待
def func6():
    driver.get("https://www.baidu.com")
    # 判断某个元素中是否可见并且是enable的，这样的话才叫clickable
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable(('link text', '高级搜索')))
    driver.find_element('link text', '高级搜索').click()


# 显示等待
def func7():
    driver.get("https://www.baidu.com")
    driver.find_element('id', 'kw').send_keys("Python")
    # 判断某个元素中的text是否包含了预期的字符串
    WebDriverWait(driver, 5).until(
        ec.text_to_be_present_in_element(('xpath', '//form[@id="form"]/div/ul/li[1]'), "是什么意思"))
    driver.find_element('xpath', '//form[@id="form"]/div/ul/li[1]').click()


# 复选框操作
def func8():
    driver.get("https://flight.qunar.com/")
    print(driver.find_element('id', 'searchTypeRnd').is_selected())  # 判断元素是否被选中
    print(driver.find_element('id', 'searchTypeRnd').is_enabled())  # 判断元素是否被使用
    print(driver.find_element('id', 'searchTypeSng').is_displayed())  # 判断元素是否被隐藏


# 复合键输入
def func9():
    driver.get("https://www.baidu.com")
    # 按住SHIFT键输入python
    driver.find_element("id", "kw").send_keys(Keys.SHIFT, "python")
    time.sleep(1)
    # 输入python 50次
    driver.find_element("id", "kw").send_keys("python" * 50)
    time.sleep(1)
    # 按住control键点击a键
    driver.find_element("id", "kw").send_keys(Keys.CONTROL, "a")
    time.sleep(1)
    # 点击delete键
    driver.find_element("id", "kw").send_keys(Keys.DELETE)


# 下拉框操作
def func10():
    driver.get("http://www.fanyunedu.com:5000/general/web")
    # 通过序号选择下拉框的值
    Select(driver.find_element('tag name', 'select')).select_by_index(1)
    time.sleep(1)
    # 通过value属性选择下拉框的值
    Select(driver.find_element('tag name', 'select')).select_by_value("sh")
    time.sleep(1)
    # 通过下拉框的text文字选择
    Select(driver.find_element('tag name', 'select')).select_by_visible_text("北京")


# Frame切换操作
def func11():
    driver.get("https://mail.qq.com")
    time.sleep(2)

    # 切换到iframe
    driver.switch_to.frame(driver.find_element('name', 'login_frame'))

    driver.find_element('id', 'u').clear()
    driver.find_element('id', 'u').send_keys('888888')

    # 切换回原本的frame
    driver.switch_to.default_content()
    driver.find_element('link text', '关于腾讯').click()


# 文件上传操作
def func12():
    driver.get("http://www.fanyunedu.com:5000/general/web")
    # 利用input标签的type属性为file，直接用send_keys()方法上传文件，但注意文件必须是使用绝对路径
    driver.find_element('xpath', '//input[@type="file"]').send_keys(
        r"/home/kirk/Desktop/learn-code/level_13/selenium_learning_img.png")


# 多窗口切换操作
def func13():
    driver.get("http://www.fanyunedu.com:5000/general/web")

    # 记录当前窗口
    old_window = driver.current_window_handle  # 保留当前窗口句柄
    driver.find_element('link text', '打开百度').click()
    time.sleep(1)

    # 切换到百度的窗口上
    driver.switch_to.window(driver.window_handles[2])  # 之前的窗口就是0,下一个窗口就是1依次计数
    driver.find_element('id', 'kw').send_keys('python')
    time.sleep(2)

    # 切换回原来的窗口
    driver.switch_to.window(old_window)
    driver.find_element('name', 'alert1').click()


# 悬浮框操作1
def func14():
    driver.get("https://www.baidu.com")
    item = driver.find_element('id', "s-usersetting-top")
    ActionChains(driver).move_to_element(item).perform()  # 模拟鼠标移动操作
    driver.find_element('link text', '高级搜索').click()


# 悬浮框操作2
def func15():
    driver.get("https://www.baidu.com")
    driver.find_element('id', 'kw').send_keys('python')
    menus = driver.find_elements('class name', 'bdsug-overflow')  # 把悬浮框中的内容通过想同的class属性值筛选出来
    for menu in menus:
        print(menu.text)  # 遍历打印悬浮框中内容的text文本

    menus[5].click()  # 通过序号直接点击对应元素


# 悬浮框操作练习
def func16():
    driver.get("https://www.qq.com")
    ActionChains(driver).move_to_element(driver.find_element('class name', 'more-txt')).perform()
    driver.find_element('link text', '车型').click()


if __name__ == '__main__':
    func16()
    # 退出进程
    time.sleep(3)  # 强制等待/固定等待
    driver.quit()
