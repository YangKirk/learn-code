Update Date:20190731

[TOC]
## 1. TimeDuration(持续时间)类
client.py下的一个类，用来描述程序执行时间，时间单位为 ms 毫秒
```python
# 引用
from vis_client.client import TimeDuration
# 使用
p = api.wait_image(env.img1, duration=60*TimeDuration.Second)
# 不限时间
TimeDuration.Forever =-1
# 1毫秒
TimeDuration.MilliSecond = 1
# 1秒
TimeDuration.Second = 1000
# 1分钟
TimeDuration.Minute = 60000
```

## 2. Point(坐标点) 类
client.py下的一个类，用来存放坐标点
``` python
# 引用
from vis_client.client import Point
# 创建对象
p = Point(50,50)
# Point类的 is_valid方法
# api.find_image没找到图返回Point(-1, -1)，
# 找到了返回图片的具体坐标Point(50, 200)

Point(-1,-1).is_valid() ==>False
Point(50,200).is_valid() ==>True
```
## 3. Rectangle(矩形) 类
client.py下的一个类，用来存放指定区域，一般用来传参，很少使用
``` python
# 引用
from vis_client.client import Rectangle, Point
# 创建对象
rect = Rectangle(Point(50,50), point(200,200))
```
## 4. VisClient 类
客户端大部分基础方法都在这里面，有兴趣自己看

## 5. VisClientApi 类 OCR
给latte project提供api的类，我们用的api方法都来自这里
``` python
# 实例化
api = VisClientApi(server的地址和端口)
api = VisClientApi('http://localhost:8080')
# 使用
api.find_image(image_path)
api.click_keys("win")
```
### 5.1 get_image_string(rect, config="")
在给定的区域执行OCR(光学字符识别)
***范例***
``` python
文本, 图片 = api.get_image_string(Rectangle(Point(0,0),Point(500,500)))
```
***参数分析***
**rect** ==>client.py 下的 Rectangle 实例
**config** ==>tesseract OCR 引擎的参数 
有兴趣请自行研究 ocr config [--psm](https://stackoverflow.com/questions/44619077/pytesseract-ocr-multiple-config-options)
***返回值***
return text, image
**text** ==>区域内识别出来的字符串
**image** ==>指定区域内的图片，格式为PIL.Image

### 5.2 get_image_string_reference(image_path,rect,**kargs)
寻找给定的图片，找到后在给定图片的返回内执行OCR(光学字符识别)
该方法原理为找到图片左上角，然后以该点为原点截取一个矩形区域，执行OCR
***范例***
```python
文本 = api.get_image_string_reference(env.img1,Rectang(Point(0,0),Point(50,50)))
print(文本)
```
***参数分析***
**rect** ==>client.py 下的 Rectangle 实例
**config** ==>tesseract OCR 引擎的参数
**match_rate** ==>相似度/匹配率/置信度   用来指定多少匹配率为找到图片，值在0到1之间
**scale_set** ==>图片缩放比例，当传入scal_set时，用于模板匹配的小图会按比例缩放，比例为机台分辨率/模板图片分辨率  **参数类型:**[]列表，列表里面包含一个或多个存放x,y比例的列表
***返回值***
**text** ==>区域内识别出来的字符串

### 5.3 get_image_all_string()
获取全屏的字符串，因性能太差，识别效果太差，所以未投入使用

## 6. VisClientApi 类 找图相关
### 6.1 find_image(image_path, **kargs)
在桌面上寻找给定的图片，返回图片左上角坐标点
***范例***

``` python
坐标点, 匹配度 = api.find_image(图片路径,similar=1, match_rate=0.8, search_area=(Point(0,0),Point(200,200)), scale_set=[[1,1]])
```
***参数分析***
**image_path** ==>图片路径，现latte project使用常量模块存放路径，env.POWER_OPTION
**similar** ==>是否返回相似度，默认不返回。similar <0 ==>不返回，similar=1 ==>返回
**match_rate** ==>相似度/匹配率/置信度   用来指定多少匹配率为找到图片，值在0到1之间
**search_area** ==>在指定区域内找图， **类型:**包含两个Point实例的元组  (Point(x1,y1),Point(x2,y2))
**scale_set** ==>图片缩放比例，当传入scal_set时，用于模板匹配的小图会按比例缩放，比例为机台分辨率/模板图片分辨率  **参数类型:**[]列表，列表里面包含一个或多个存放x,y比例的列表

``` python
# 先把图片x,y都放大1.2倍去匹配，没找到图就放大1.5再去找，如果都没找到就返回Point(-1,-1)
scale_set = [[1.2,1.2],[1.5,1.5]]
```
***返回值***
**point**  ==>目标图片在屏幕上的左上角坐标点   **类型:**client.py下Point类的实例  例如  Point(123,123)
**similar**  ==>当传入参数similar=1时，会返回(point,similar)，**类型:**float 浮点型

### 6.2 find_first_of_images(images_path, **kargs)
传入一个图片列表，寻找多张图，返回最先找到的图的坐标
***范例***
```python
if api.find_first_of_images([env.img1,env.img2,env.img3]).is_valid():
	print("有图片找到啦!")
else:
	print("抱歉，所有图片都没找到。")
```
***参数分析***
**images_path** ==>装有图片的列表  **type:** list   [env.img1, env.img2]
**similar** ==>是否返回相似度，默认不返回。similar <0 ==>不返回，similar=1 ==>返回
**match_rate** ==>相似度/匹配率/置信度   用来指定多少匹配率为找到图片，值在0到1之间
**search_area** ==>在指定区域内找图， **类型:**包含两个Point示例的元组  (Point(x1,y1),Point(x2,y2))
**scale_set** ==>图片缩放比例，当传入scal_set时，用于模板匹配的小图会按比例缩放，比例为机台分辨率/模板图片分辨率  **参数类型:**[]列表，列表里面包含一个或多个存放x,y比例的列表
***返回值***
**point**  ==>最新找到的图片在屏幕上的左上角坐标点   **类型:**client.py下Point类的实例  例如  Point(123,123)
**similar**  ==>当传入参数similar=1时，会返回(point,similar)，**类型:**float 浮点型

### 6.3 find_images(images_path, **kargs)
传入一组图片，返回所有图片的结果
***范例***

```python
# 传入一组图片，点击所有找到的图
point_list = api.find_images([env.img1,env.img2],match_rate=0.8)
for point in point_list:
	if point.is_valid():
		api.click_mouse_buttons(Point)
```
***参数分析***
**images_path** ==>装有图片的列表  **type:** list   [env.img1, env.img2]
**similar** ==>是否返回相似度，默认不返回。similar <0 ==>不返回，similar=1 ==>返回
**match_rate** ==>相似度/匹配率/置信度   用来指定多少匹配率为找到图片，值在0到1之间
**search_area** ==>在指定区域内找图， **类型:**包含两个Point实例的元组  (Point(x1,y1),Point(x2,y2))
**scale_set** ==>图片缩放比例，当传入scal_set时，用于模板匹配的小图会按比例缩放，比例为机台分辨率/模板图片分辨率  **参数类型:**[]列表，列表里面包含一个或多个存放x,y比例的列表
***返回值***
**point_list**  ==>所有图片匹配的结果列表  **type:**list 列表   [Point(-1,-1), Point(20,30), Point(100,200)]

### 6.4 wait_image(image_path,duration=5*TimeDuration.Second,cb=None,*args,**kargs)
等待图片出现，可以一边等一边执行函数
***范例***

```python
# 以0.8的匹配度寻找win_icon图片，没找到就点击"enter"键，如果在20秒之内没找到图片，就抛出ImageNotFound的异常
if not api.wait_image(env.win_icon,duration=20*TimeDuration.Second,
					  click_keys,"enter",match_rate=0.8).is_valid():
	raise ImageNotFound()
```
***参数分析***

**image_path** ==>图片路径
**duration** 找图持续时间，使用TimeDuration类下的常量
**cb** ==>callback 回调函数，找图过程中需要执行的函数
**\*args ** ==>传递给回调函数的参数，例如 cb=click_keys args=("enter") 回调函数为按键，本参数为"enter"键
**\*\*kargs** ==> 多个关键字参数，如下面的参数
**match_rate** ==>相似度/匹配率/置信度   用来指定多少匹配率为找到图片，值在0到1之间
**search_area** ==>在指定区域内找图， **type:**包含两个Point实例的元组  (Point(x1,y1),Point(x2,y2))
**scale_set** ==>图片缩放比例，当传入scal_set时，用于模板匹配的小图会按比例缩放，比例为机台分辨率/模板图片分辨率  **type:**[]列表，列表里面包含一个或多个存放x,y比例的列表
***返回值***
**point**  ==>目标图片在屏幕上的中心点   **类型:**client.py下Point类的实例  例如  Point(123,123)

### 6.5 wait_first_of_images(image_path,duration=5*TimeDuration.Second,cb=None,*args,**kargs)
传入一个图片list，在给定时间内找多张图，找到一张后就返回该张图片的坐标
***范例***
```python
# 20秒内以0.8的匹配率找多张图，没找到图就点击"enter"键，20秒内没找到就抛出ImageNotWaited异常
if not api.wait_first_of_images([env.img1,env.img2],duration=20*TimeDuration.Second, cb=click_keys, "enter", match_rate=0.8).is_valid():
	raise ImageNotWaited()
```
***参数分析***
**image_path** ==>存放有多张图片的列表
**duration** 找图持续时间，使用TimeDuration类下的常量
**cb** ==>callback 回调函数，找图过程中需要执行的函数
**\*args** ==>传递给回调函数的参数，例如 cb=click_keys args=("enter") 回调函数为按键，本参数为"enter"键
**\*\*kargs** ==> 多个关键字参数，如下面的参数
**match_rate** ==>相似度/匹配率/置信度   用来指定多少匹配率为找到图片，值在0到1之间
**search_area** ==>在指定区域内找图， **type:**包含两个Point示例的元组  (Point(x1,y1),Point(x2,y2))
**scale_set** ==>图片缩放比例，当传入scal_set时，用于模板匹配的小图会按比例缩放，比例为机台分辨率/模板图片分辨率  **type:**[]列表，列表里面包含一个或多个存放x,y比例的列表
***返回值***
**point**  ==>目标图片在屏幕上的中心点   **类型:**client.py下Point类的实例  例如  Point(123,123)

### 6.6 wait_images()
该函数使用方法与wait_first_of_images()类似，只有返回值不一样
***返回值***
**point_list**  包含所有图片查找结果的list   **type:**list

### 6.7 wait_image_disappear()
等待给定的图片消失
***范例***
```python
api.wait_image_disappear(env.WINKEY)
print("计算机已经退出桌面")
```
***参数分析***
与上面的多个wait_image方法参数一样
***返回值***
不管图片是否消失，都会返回Point(-1,-1)，预计后面后优化为返回True或False。

### 6.8 wait_images_disappear()
等待所有给定的图片消失
***范例***
```python
api.wait_images_disappear([env.img1,env.img2],duration=20*TimeDuration.Second)
print("所有图片都已消失")
```
***参数分析***
**images_path** 包含多张图片的list  **type:**list
其他和wait_image的参数相同
***返回值***
不管图片是否消失，都会返回[Point(-1,-1),(-1,-1)]，预计后面后优化为返回True或False。

### 6.9 screenshot()
用摄像头拍一张照片，并剪切出测试机屏幕部分，返回PIL.Image图片实例对象
***范例***
```python
image = api.screenshot()
# 显示图片
image.show()
```
***返回值***
PIL.Image

### 6.10 rawimage()
用摄像头拍一张照片，返回PIL.Image图片实例对象
***范例***
```python
image = api.rawimage()
# 显示图片
imgage.show()
```
***返回值***
PIL.Image

### 6.11 get_last_image()
获取摄像头最后一张拍的照片
***范例***
```python
image = api.get_last_image()
# 显示图片
imgage.show()
```
***返回值***
PIL.Image

### 6.12 draw_rectangle(image,rect)
传入图片对象和坐标，该函数会为其画矩形框
***范例***
```python
from PIL import Image
from vis_client.client import Rectangle,Point
img = Image.open(r"D:\image_path")
rect = Rectangle(Point(0,0),Point(50,50))
api.draw_rectangle(img,rect)
pring("上面的函数会为img图片画上红色的矩形框")
```
***参数分析***
**image** 图片对象 PIL.Image
**rect** 矩形类实例对象

### 6.13 draw_point(image,p)
传入图片和坐标点，该函数会在图片的坐标点圆
***参数分析***
**image** 图片对象 PIL.Image
**p** 坐标点 Point类实例对象

## 7. VisClientApi 类 HID 按键相关
### 7.1 hid_command(cmd_str)
发送指令到STM32单片机
***范例***
```python
# 重启HID
hid_command("{16,1}")
```
***参数分析***
**cmd_str** ==> 单片机指令的字符串形式 "{xx,xx,xx}" STM32F103C8自用_.docx 里面包含所有指令

### 7.2 click_keys(*keys, **kargs)
点击按键，分为虚拟键盘和电磁铁两类
***范例***
```python
# 使用虚拟键盘按下win键和r键
api.click_keys("win", "r") 
# 使用电磁铁按下测试机down方向键和p键
api.click_keys("win", "p", force_physical=True)
```
***参数分析 ***
**\*keys** ==>多参数，传入1~6个键，模拟按键   api.click_keys("key1", "key2","key3", "key4")
**\*\*kargs** ==>多关键字参数，目前只有一个 force_physical, 值为True时用电磁铁，默认使用虚拟键盘

### 7.3 press_keys(duration=1*TimeDuration.Secend, *keys, **kargs)
持续按压按键，分为虚拟键盘和电磁铁两类
***范例***
```python
# 使用虚拟键盘按下win键和r键不弹起
api.press_keys("win", "r") 
# 使用电磁铁按下测试机down方向键和p键不弹起
api.press_keys("win", "p", force_physical=True)
```
***参数分析***
**duration** ==>按压持续时间  **type:** TimeDuration.Forever/Second/Minute
**\*keys** ==>多参数，传入1~6个键
**\*\*kargs** ==>多关键字参数，目前只有一个 force_physical, 值为True时用电磁铁，默认使用虚拟键盘

### 7.4 click_keys_duration(duration=0.1*TimeDuration.Second,*keys,**kargs)
在给定时间内不断点击按键，非按住不放，分为虚拟键盘和电磁铁
***范例***
```python
# 不断用电磁铁点击测试机键盘的"enter"键两秒钟
api.click_keys_duration(duration=2*TimeDuration.Second,"enter",force_physical=True)
```
***参数分析***
**duration** 持续时间
***keys* 要按的键
** **keys** 只有force_physical  是否使用电磁铁
***返回值***
**counter**  点了多少次


### 7.5 release_all_keys()
释放所有已按下的键
***范例***
```python
api.press_keys("win","up",duration=TimeDuration.Second)
api.release_all_keys()
```

### 7.6 send_word(word)
传送要输入的字符串给单片机，然后又单片机模拟输入到被控制机
***范例***

```python
api.send_word("This PC")
api.click_keys("enter")
print("进入我的电脑界面")
```
***参数分析***
**word** 要输入到被控制机的字符串  **type:** str

### 7.7 click_mouse_buttons(point, times, *buttons, **kargs)
使用单片机模拟鼠标操作，分为相对移动和绝对移动
相对移动 ==>windows系统下移动固定的百分比，不受分辨率影响
***范例***
```python
# 鼠标移动到(0,0)点，不点击
api.click_mouse_buttons(Point(0,0),1,"none")
# 鼠标移动到(50,50)点，并点击左键
api.click_mouse_buttons(Point(50,50),1,"left")
```
***参数分析***
**point** ==>要点击的点 **type:** clinet.py下的Point类实例对象  Point(0,0)
**times** ==>点击的次数 **type:** int
**\*buttons** ==>点击的按键  "left" ->左键 "right"->右键 "middle"->中键 "none"->不点击  **type:** str 字符串
**\*\*kargs**  目前只有relatively==True>使用相对移动False使用绝对移动，默认绝对移动。
绝对移动==>给定坐标，移动到该坐标  相对移动==>给定(5,5)，从当前位置移动分别向右向下移动5像素

### 7.8 click_mouse_button_at_image(image_path,times,*buttons,duration,**kargs)

在屏幕上寻找图片，找到之后进行鼠标点击
***范例***

```python
# 以0.9的匹配度找YES按钮20秒，找到后就点击它
if api.click_mouse_button_at_image(env.YES,1,"left",duration=20*TimeDuration.Second,match_rate=0.9).is_valid()
	print("已经点击Yes按钮")
```

***参数分析***
**image_path** ==>图片路径  **type:**str
**times** ==>点击次数
**buttons** ==>鼠标按键  "left" "right" "middle" "none"
**duration** ==>找图持续时间
**\*\*kargs**  ==>找图的参数设置 match_rate 匹配度  search_area 限制找图范围

***返回值***
没找到图返回Point(-1,-1) 找到返回图片的中心点

### 7.9 click_mouse_button_at_images(images_path,times,*buttons,duration,**kargs)
在屏幕上找多张图，点击找到的第一张图
***范例***
```python
# 找img1和img2一分钟，找到其中一张就执行鼠标点击，点击后函数结束。
api.click_mouse_button_at_images([env.img1,env.img2],1,"left",1*TimeDuration.Minute)
```
***参数分析***
**image_path** ==>存放多张图片路径的列表  **type:**list
**times** ==>点击次数
**buttons** ==>鼠标按键  "left" "right" "middle" "none"
**duration** ==>找图持续时间
**\*\*kargs**  ==>找图的参数设置 match_rate 匹配度  search_area 限制找图范围

***返回值***
找到图返回图片中心坐标点，没找到返回Point(--1,-1)

## 8. VisClientApi 设置相关
### 8.1 find_cornor()
供定点工具使用。用摄像头拍一张照片，然后自动给屏幕定点。

### 8.2 set_cornor(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y)
供定点工具使用。设置屏幕的四个点。

### 8.3 get_cornor()
供定点工具使用。获取屏幕的四个点

### 8.4 set_config(**kargs)
设置底层vis_server信息，例如拍照模式，摄像头曝光度等
***范例***
```python
# 设置摄像头拍照模式，曝光时间
api.set_config(photo_mode=2,cam_exposure_time=15000)
```
***参数分析***
**\*\*kargs** 多关键字参数，具体参数请参考api.get_config()列出的信息或server端VisConfig类
常用的一些参数
**photo_mode** ==>拍照模式，0为不使用摄像头，1为单张拍照，2为连续拍照
**cam_exposure_time** ==>曝光时间，-1为自动曝光，300~100000为手动固定曝光时间
**cam_num_images** ==>连续拍照模式下拍摄多少张图片后获取图片为模板匹配的大图
**tmp_img_file** ==> server端读取的摄像头拍摄的图片，可设为自己的图片，配合photo_mode=0使用

### 8.5 get_config()
获取server端的配置信息，配合api.set_config()使用
***范例***

```python
config = api.get_config()
print(config)
```
