# 一、自动化测试概念

## 1.什么是自动化测试？

![image-20220506211226629](Web_UI自动化测试.assets/image-20220506211810499.png)



## 2.什么项目适合自动化?

![image-20220506211259081](Web_UI自动化测试.assets/image-20220506211259081.png)



## 3.自动化测试的类型划分

![image-20220506211410814](Web_UI自动化测试.assets/image-20220506211410814.png)



## 4.自动化测试用例的设计原则

![image-20220506211810499](Web_UI自动化测试.assets/image-20220506211810499.png)



------

# 二、Web自动化测试的环境设置(Selenium)

## 1. Windows系统

- ### 通过pip install selenium安装最新的selenium包(Python)

- ### 下载对应的chromedriver或geckodriver, 并将driver放到环境变量的路径中

  - chromedriver下载路径:
    - http://npm.taobao.org/mirrors/chromedriver/
    - http://npm.taobao.org/mirrors/geckodriver/

- 在pycharm中导入webdriver即可使用

  ```python
  from selenium import webdriver
  ```



## 2. Linux系统

- ### pip install selenium

- ### 去http://chromedriver.storage.googleapis.com/index.html下载对应版本的Linux chrome驱动

- ### 解压驱动得到chromedriver文件

- ### 打开终端输入以下指令: 

  ```
  sudo chmod 777 chromedirver
  ```

  ```
  sudo cp chromedriver /usr/bin(路径需要填写正确)
  ```

- ### 环境变量配置完成



------

# 三、Webdriver的工作原理

![image-20220506213326498](Web_UI自动化测试.assets/image-20220506213326498.png)



------

# 四、Web自动化测试的LOVE四步法

![image-20220506213415859](Web_UI自动化测试.assets/image-20220506213415859.png)

## 0. Webdriver常用 API-浏览器操作

```python
# 打开url
driver.get(url)

# 关闭
driver.quit()	# 结束进程
driver.close()	# 仅关闭当前窗口

# 设置窗口大小
driver.set_window_size(200, 500)	# 设置窗口大小为宽200,高500

# 最大化窗口
driver.maximize_window()

# 获取网页源码
driver.page_source	# 属性，不用加括号（）

# 获取窗口名称
driver.name		# 属性，不用加括号（）

# 获取节点上的文本信息
driver.text

# 刷新页面
driver.refresh()

# 获取页面标题
driver.title	# 属性，不用加括号（）

# 获取当前页面url地址
driver.current_url		# 属性，不用加括号()

# 获取元素的属性信息
driver.get_attribute(name)

# 判断元素是否显示出来
driver.is_displayed		# 属性，不用加括号()

# 获取当前页面截图
driver.get_screenshot_as_file(path)		# 不写path默认保存在当前路径下
```

```python
# 代码举例
from selenium import webdriver		# 导入webdriver模块
import time		# 导入时间库

driver=webdriver.Chrome()		# 新建一个webdriver的实例

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

# 定位到属性id值为su的元素并获取此元素的value值
print(driver.find_element('id', 'su').get_attribute("value"))  

# 定位到超链接text描述为贴吧的元素并打印此元素的text值
print(driver.find_element('link text', '贴吧').text)  

# 定位到属性id值为form的元素并判断此元素是否为隐藏，返回True or False
print(driver.find_element('id', 'form').is_displayed())  

driver.find_element('id', 'su').click()  # 定位到属性id值为su的元素并点击它

print(driver.name)  # 打印窗口名
print(driver.title)  # 打印页面标题
print(driver.current_url)  # 打印当前窗口地址
driver.get_screenshot_as_file('selenium_learning_img.png')	# 截图当前页面

# 等待10秒关闭浏览器
time.sleep(10)
driver.quit()  # 关闭进程
# driver.close()  # 关闭当前窗口(浏览器)
```



## 0.5 元素定位基础知识(HTML前端相关知识)

### a. HTML页面基本结构

```htm
<html>
	<head></head>	--> html文档头部区域，在页面中不可见
	<body></body>	--> html文档内容部分，页面中可见
</html>
```



### b. 常见的页面元素

- #### 容器型元素: div(自定义容器), form(表单), table(表格)

- #### 页面元素：link(a 超链接), img(图片), input输入域(button(按钮), text(文本), file(文件)), select(下拉框), checkbox(单选框(yes or no)), radio(复选框), textarea(文本框), submit(提交按钮)



### c. HTML，CSS 和Java Script之间的关系?

- #### HTML组成了页面的基本结构，类似人身体的骨架血肉

- #### CSS是层叠样式表，决定了页面元素显示的外观及位置，相当于美容化妆品

- #### Java Script(简称JS), 主要用于自定义页面元素的行为



### d. 什么是前端？什么是后端？

- #### 前端: 也叫客户端，就是所有与最终用户直接交互的部分

- #### 后端: 也叫服务器端，不直接与最终用户交互，在内部进行调用和数据处理的部分



## 1.(L)元素定位(Locate)----八大元素定位法

- ### 元素定位的方法有很多，总的原则是怎么简单怎么来

- ### 为什么xpath和 css selector是万能的？

  - #### 可以通过位置进行定位

  - #### 可以通过任意属性进行定位

### a. id定位

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com")  # 打开B站主页

# id定位
print(driver.find_element('id', 'i_cecream'))  # 定位id为i_cecream的元素
```



### b. name定位

```python
# name定位
print(driver.find_element('name', 'keywords'))  # 定位name为keywords的元素
```



### c. class name定位(特指具有class属性的元素)

```python
# class name定位
print(driver.find_element('class name', 'old-browser-tip'))  
# 定位class属性为old-browser-tip的元素

# 对于复合样式(例如:bili-header large-header)不能直接使用class name来进行定位
print(driver.find_element('class name', 'bili-header large-header'))    # 会报错
```



### d. tag name

```python
# tag name定位: 一般用于查找同类元素
print(len(driver.find_elements('tag name', 'input')))  # 定位tag name属性为input的元素
```



### e. link text`<a>`

```python
# link text定位(属性值精准定位):用于定位超链接a标签
driver.find_element('link text', '番剧').click()  # 点击link text属性为番剧的超链接
```



### f. partial link text`<a>`

```python
# partial link text定位(属性值可以为部分)：用于定位超链接a标签
driver.find_element('partial link text', '直').click()   
# 点击link text属性包含直这个字的超链接
```



### g. xpath (万能，可以在chrome中使用$x调试)

- ### xpath语法

  ```python
  # 绝对路径表示法：指从/目录开始的路径表示法(通常是/html),必须根据实际路径逐级表示
  print(driver.find_element('xpath', '/html/body/div'))   
  # 定位绝对路径为/html/body/div的元素
  
  # 相对路径表示法:指从目标对象所在位置根据其父对象进行路径表示的方法
  driver.find_element('xpath', '//body/div[2]//li[2]').click()    # 点击番剧的相对路径
  
  # xpath属性定位法
  driver.find_element('xpath', '//div[@class="header-login-entry"]').click()  
  # 定位div标签class属性为header-login-entry的元素并点击
  time.sleep(2)
  driver.find_element('xpath', '//input[@type="text"][@placeholder="请输入账号"]').click()
  # 定位input标签属性type值为text，placeholder属性值为请输入账号的元素并点击
  driver.find_element('xpath', '//*[@placeholder="请输入账号"]').clear()
  # 定位placeholder属性值为请输入账号的元素并清空
  driver.find_element('xpath', '//*[@placeholder="请输入账号"]').send_keys("12345678900")
  # 定位placeholder属性值为请输入账号的元素并输入12345678900
  
  # # xpath属性模糊定位
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
  
  ```

- #### xpath可以在浏览器中使用Console功能调试($x())

  ![image-20220507192857577](Web_UI自动化测试.assets/image-20220507192857577.png)

### h. css selector (万能，可以在chrome中使用$$调试)

- ### 利用元素的标签、或元素的单一属性定位(id、class等)

  ```python
  # 利用元素标签来定位所有相同元素
  div = driver.find_elements('css selector', 'div')   # 定位标签为div的元素，返回列表
  # print(len(div))
  
  # 利用class属性来进行定位(css样式需要加.作为开头)
  
  # 定位class属性为banner-link的元素并点击
  driver.find_element('css selector', '.banner-link').click() 
  
  # 定位class属性为right-entry__outside go-login-btn的复合css样式并点击
  driver.find_element('css selector', '.right-entry__outside.go-login-btn').click()
  
  # 利用id属性来进行定位(用#号表示id属性后跟id属性值)
  print(driver.find_element('css selector', '#i_cecream'))
  ```

  

- ### 利用多属性定位

  ```python
  # 多属性定位
  # 定位target属性为_blank，class属性为default-entry的第一个元素并点击
  driver.find_elements('css selector', "[target='_blank'][class='default-entry']")[0].click()
  ```

  

- ### 利用标签+属性组合定位

  ```python
  # 组合定位，先用id定位父级，再用class属性定位子级，无法定位的再考虑位置定位
  driver.find_element('css selector',
                      '#i_cecream > div.bili-header.large-header > div.bili-header__bar '
                      '> ul.right-entry > li:nth-child(1) > li > div > div').click()
  ```

  

- ### 利用层级位置(父子\孙子)关系定位

  ```python
  # 利用父子位置关系来定位(父子关系 > 号连接)
  print(driver.find_element('css selector', 'body > iframe').tag_name)
  driver.find_element('css selector',
                      'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) '
                      '> ul:nth-child(3) > li:nth-child(1) > li > div > div').click()
  # 注意nth-child()的序号，从1开始，其他的标签也要计数，例如body下第4个标签是要进入的div子级，但是只数div可能是第2个，这里需要填写的序号应该为4
  
  # 利用孙子位置关系来定位(孙子关系 空格连接)
  driver.find_element('css selector', 'ul.right-entry div.header-login-entry').click()
  ```



- ### 模糊匹配定位，相当于xpath中的contains()

  ```python
  # 模糊匹配，相当于xpath中的contains
  driver.find_element('css selector', 'div[class*="header-login-entry"]').click()
  ```

  

- ### css selector也可以在浏览器中使用Console功能调试($$())

  ![image-20220507203409402](Web_UI自动化测试.assets/image-20220507203409402.png)



## 1.5.元素定位总结

![image-20220507203237269](Web_UI自动化测试.assets/image-20220507203237269.png)