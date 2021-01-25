# -*- coding: utf-8 -*-
"""
-----------------------------------------
    File Name:      datetime_image.py
    Description:
    Author:         Kirk
    Date:           2020/10/20
-----------------------------------------
    Change Activity:
                    2020/10/20
-----------------------------------------
"""
from datetime import datetime, timedelta
from PIL import Image, ImageFilter

# datetime模块
now = datetime.now()
# print(now)

t = now + timedelta(days=1, hours=2)
# print(t)


# PIL/Image 模块
im = Image.open(fp='1.jpg')  # 打开一个jpg文件，当前路径下

# 获取图片尺寸
w, h = im.size
# print('Image size : %s * %s' % (w, h))

# 缩放到50%
im.thumbnail((w // 2, h // 2))
# print('Image size : %s * %s' % (w // 2, h // 2))

# 缩放后的图片jpg格式另存为
# im.save('thumbnail_1.jpg', 'jpeg')

# 图片模糊效果
im2 = im.filter(ImageFilter.BLUR)
# im2.save('1_blur.jpg', 'jpeg')
