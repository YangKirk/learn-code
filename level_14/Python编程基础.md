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



## 3、字符串类型（String）

![](/home/kirk/Desktop/learn-code/level_14/4.png)

```python
s = "'hello, world'"  # 要求以-1为步长，按字符串内容去掉单引号后反序输出，显示结果
print(s[1:-1][::-1])	# dlrow ,olleh
```



### a.字符串常用函数

```python
len(string)			# 返回字符串的长度
# 举例
s = 'hello, welcome to study testing'
print(len(s))	# 31

count(str, beg=0, end=len(string))	# 返回str在string里面出现的次数，如果beg或者end指定则返回指定范围内str出现的次数
# 举例
print(s.count('l', 8, len(s) - 1))	# 1

capitalize()		# 将字符串的第一个字符转换为大写
# 举例
print(s.capitalize())	# Hello, welcome to study testing

find(str, beg=0,end=len(string))	# 检测str是否包含在字符串中，如果beg和end指定范围，则检查是否包含在指定范围内，如果是则返回开始的索引值，否则返回-1
# 举例
print(s.find('a'))	# -1

replace('old_string','new_string') 	# 将字符串中的old_string 替换为new_string
# 举例
print(s.replace(',', ''))	# hello welcome to study testing

split(str='')	# 以str为分隔符拆分字符串, 返回字符串拆分后的列表
# 举例
l = s.split(' ')	# ['hello,', 'welcome', 'to', 'study', 'testing']

index(str, beg=0,end=len(string))	# 跟find()方法相同，但是如果str不在字符串中会报一个异常

','.join(['a','b','c'])		# 以指定符号连接后面列表中的字符串元素，以字符串形式返回
# 举例
print('#'.join(l))	# hello,#welcome#to#study#testing

isdigit()		# 如果字符串只包含数字则返回True否则返回False
# 举例
t = '1234a'
print(t.isdigit())	# False

isalpha()		# 判断字符串中是否只包含字母

islower()	# 如果字符串中包含至少一个区分大小写的字符，并且所有这些字符都是小写，则返回True，否则False

isspace()	# 如果字符串中只包含空格，则返回True，否则返回False

istitle()	# 如果字符串是标题化(首字母大写后续全是小写)的则返回True

lower()		# 转换字符串中所有大写字符为小写

upper()		# 转换字符串所有小写字符为大写

startswith()	# 检查字符串是否以指定str开头，返回True/False

strip(str)		# 删除字符串两把的str代表的字符，如果不指定str则删除空白字符
# 举例
print(t.strip('a'))		# '1234'

rstrip()和lstrip()	#删除字符串右边或者左边的str
```



## 4、列表类型(List)

![](/home/kirk/Desktop/learn-code/level_14/5.png)



### a.列表的常用函数

```python
list.append(object)  # 在列表末尾添加新的对象
# 举例
list1 = ['hello', 'python', 'java', 'world']
list1.append('x')
print(list1)	# ['hello', 'python', 'java', 'world', 'x']

list.count(object)  # 统计某个元素在列表中出现的个数
# 举例
print(list1.count('java'))	# 1

list.extend(seq)  # 在列表末尾一次性追加另一个序列的多个值(用新列表扩展原来的列表)
# 举例
list2 = ['x']
list1.extend(list2)		# ['hello', 'python', 'java', 'world', 'x']

list.index(object)  # 从列表中找出某个值第一个匹配项的索引位置，索引从0开始
# 举例
print(list1.index('java'))	# 2

list.insert(index, object)  # 将对象插入列表某个索引位置
# 举例
list1.insert(0, list2)	# [['x'], 'hello', 'python', 'java', 'world']

list.pop(index)  # 移除列表中的一个元素(默认最后一个元素),并且返回该元素的值
# 举例
print(list1.pop(0))		# hello
print(list1)		# ['python', 'java', 'world']

list.remove(object)  # 移除列表中某个值的第一个匹配项
# 举例
list1.remove('java')	# ['hello', 'python', 'world']

list.reverse()  # 反向列表中的元素
# 举例
list1.reverse()		# ['world', 'java', 'python', 'hello']

list.sort()  # 对原列表进行排序(无返回值)
# 举例
list1.sort()	# ['hello', 'java', 'python', 'world']
list1.sort(reverse=True)	# ['world', 'python', 'java', 'hello']

list.copy()		# 复制一个列表
# 举例
list3 = list1.copy()

list.clear() # 清楚列表中所有元素
# 举例
list1.clear()	# []

max(list)  # 求列表的最大值
# 举例
list4 = [1, 3, 4, 66, 2, 4, 5]
print(max(list4))	# 66

min(list)  # 求列表最小值
# 举例
print(min(list4))	# 1

sum(list)  # 求列表的和
# 举例
print(sum(list4))	# 85

len(list)  # 求列表中元素个数
# 举例
print(len(list4))	# 7

list(str)  # 将字符串强制转换为列表
# 举例
s = 'java'
print(list(s))	# ['j', 'a', 'v', 'a']

list(range(start, end))  # 快速生成指定范围内数字列表
# 举例
print(list(range(1,10)))	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

