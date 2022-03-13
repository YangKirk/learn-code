# Python基础

## 程序的基本概念和开发环境搭建

![](/home/kirk/Desktop/learn-code/level_14/1.png)

```python
"""
如何从一堆数字中找到最大的那个数？ [1, 3, 17, 4, 34, 56]
"""
# 1
a = [1, 3, 17, 4, 34, 56]
max_ = a[0]
for _ in a:
	if _ > max_:
		max_ = _
print(max_)

# 2
a = [1, 3, 17, 4, 34, 56]
a = max(a)
print(a)
```

```python
"""
占位符 ， 输入/输出
"""
a = 100 / 3
b = 'xxxx'
print(f'学生评分：{a:.2f}', end='  ')
print(f'学生姓名：{b}')
```





## 数据类型

## 1、数据类型定义

![](/home/kirk/Desktop/learn-code/level_14/2.png)

```python
"""
不可变数据类型
Number string tuple
"""
a = 1
print(id(a))  # 每个变量Id值一定是唯一的，如果两个变量ID是不同的，则一定是两个不同的变量
print(a)

a += 1
print(id(a))
print(a)

b = 2
print(id(b))  # a的值改变以后和b的值相同，则指向同一个内存地址(ID)
print(b)
```



```python
"""
可变数据类型
list set dictionary 
"""
a = [1, 2, 3]
print(id(a))  # 列表a的值有变化后，依然指向同一个内存地址(id)
print(a)

a.append(4)
print(id(a))
print(a)
```

## 2、数值类型(Number)

![](/home/kirk/Desktop/learn-code/level_14/3.png)



### a.数值类型常用方法及常用模块

```python
import math		# 调用数学模块
math.ceil(x)		# 取大于等于x的最小整数值，如果x是一个整数则返回x
# 举例
print(math.ceil(4.5))  # 5
print(math.ceil(-2.1))  # -2

math.fabs(x)		# 返回x的绝对值
# 举例
print(math.fabs(-2))	# 2.0

math.floor(x)		# 取小于等于x的最大整数值，如果x是一个整数则返回x
# 举例
print(math.floor(-2.2))	# -3
print(math.floor(3.1))	# 3


math.pow(x,y)		# 返回x**y，即x的y次方
# 举例
print(math.pow(2,2))	# 4.0

math.sqrt(x)		# 求x的平方根
# 举例
print(math.sqrt(4))		# 2.0
```



```python
import random		# 调用随机数模块
random.random()		# 返回[0.0, 1.0)之间的浮点数，注意这是一个左闭右开区间，随机数可能为0但不可能为1

random.randit(a,b)		# 生成一个a与b之间的随机整数，也就是[a,b]

random.randrange(a,b)	# 生成的随机整数不会包含b, 也就是[a,b)

random.uniform(a,b)		# 生成[a,b]之间的随机浮点数

random.choice([])		# 从列表中随机取出一个元素

random.shuffle([])		# 打乱列表中元素的排序

random.sample([],n)		# 从列表中随机取出n个元素
```

