# Python基础

## 一、程序的基本概念和开发环境搭建

![](/home/kirk/Desktop/learn-code/level_14/1.png)

#### 1、如何从一堆数字中找到最大的那个数？ [1, 3, 17, 4, 34, 56]

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

#### 2、占位符 ， 输入/输出

```python
"""
占位符 ， 输入/输出
"""
a = 100 / 3
b = 'xxxx'
print(f'学生评分：{a:.2f}', end='  ')
print(f'学生姓名：{b}')
```





## 二、数据类型

### 1、数据类型定义

![](/home/kirk/Desktop/learn-code/level_14/2.png)

#### a.不可变数据类型(Number/String/Tuple)

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

#### b.可变数据类型(List/Set/Dictionary)

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

### 2、数值类型(Number)

![](/home/kirk/Desktop/learn-code/level_14/3.png)



#### a.数值类型常用方法及常用模块

- ```python
  import math		# 调用数学模块
  math.ceil(x)		# 取大于等于x的最小整数值，如果x是一个整数则返回x
  # 举例
  print(math.ceil(4.5))  # 5
  print(math.ceil(-2.1))  # -2
  ```

- ```py
  math.fabs(x)		# 返回x的绝对值
  # 举例
  print(math.fabs(-2))	# 2.0
  ```

- ```python
  math.floor(x)		# 取小于等于x的最大整数值，如果x是一个整数则返回x
  # 举例
  print(math.floor(-2.2))	# -3
  print(math.floor(3.1))	# 3
  ```

- ```python
  math.pow(x,y)		# 返回x**y，即x的y次方
  # 举例
  print(math.pow(2,2))	# 4.0
  ```

- ```python
  math.sqrt(x)		# 求x的平方根
  # 举例
  print(math.sqrt(4))		# 2.0
  ```

- ```python
  import random		# 调用随机数模块
  random.random()		# 返回[0.0, 1.0)之间的浮点数，注意这是一个左闭右开区间，随机数可能为0但不可能为1
  ```

- ```python
  random.randit(a,b)		# 生成一个a与b之间的随机整数，也就是[a,b]
  
  random.randrange(a,b)	# 生成的随机整数不会包含b, 也就是[a,b)
  
  random.uniform(a,b)		# 生成[a,b]之间的随机浮点数
  
  random.choice([])		# 从列表中随机取出一个元素
  
  random.shuffle([])		# 打乱列表中元素的排序
  
  random.sample([],n)		# 从列表中随机取出n个元素
  ```

### 3、字符串类型（String）

![](/home/kirk/Desktop/learn-code/level_14/4.png)

- #### 要求以-1为步长，按字符串内容去掉单引号后反序输出，显示结果

```python
s = "'hello, world'"  # 要求以-1为步长，按字符串内容去掉单引号后反序输出，显示结果
print(s[1:-1][::-1])	# dlrow ,olleh
```



#### a.字符串常用函数

- ```python
  len(string)			# 返回字符串的长度
  # 举例
  s = 'hello, welcome to study testing'
  print(len(s))	# 31
  ```
  
- ```python
  count(str, beg=0, end=len(string))	# 返回str在string里面出现的次数，如果beg或者end指定则返回指定范围内str出现的次数
  # 举例
  print(s.count('l', 8, len(s) - 1))	# 1
  ```

- ```python
  capitalize()		# 将字符串的第一个字符转换为大写
  # 举例
  print(s.capitalize())	# Hello, welcome to study testing
  ```
- ```python
  find(str, beg=0,end=len(string))	# 检测str是否包含在字符串中，如果beg和end指定范围，则检查是否包含在指定范围内，如果是则返回开始的索引值，否则返回-1
  # 举例
  print(s.find('a'))	# -1
  ```
- ```python
  replace('old_string','new_string') 	# 将字符串中的old_string 替换为new_string
  # 举例
  print(s.replace(',', ''))	# hello welcome to study testing
  ```
- ```python
  split(str='')	# 以str为分隔符拆分字符串, 返回字符串拆分后的列表
  # 举例
  l = s.split(' ')	# ['hello,', 'welcome', 'to', 'study', 'testing']
  ```
- ```python
  index(str, beg=0,end=len(string))	# 跟find()方法相同，但是如果str不在字符串中会报一个异常
  
  ','.join(['a','b','c'])		# 以指定符号连接后面列表中的字符串元素，以字符串形式返回
  # 举例
  print('#'.join(l))	# hello,#welcome#to#study#testing
  ```
- ```python
  isdigit()		# 如果字符串只包含数字则返回True否则返回False
  # 举例
  t = '1234a'
  print(t.isdigit())	# False
  ```
- ```python
  isalpha()		# 判断字符串中是否只包含字母
  
  islower()	# 如果字符串中包含至少一个区分大小写的字符，并且所有这些字符都是小写，则返回True，否则False
  
  isspace()	# 如果字符串中只包含空格，则返回True，否则返回False
  
  istitle()	# 如果字符串是标题化(首字母大写后续全是小写)的则返回True
  
  lower()		# 转换字符串中所有大写字符为小写
  
  upper()		# 转换字符串所有小写字符为大写
  
  startswith()	# 检查字符串是否以指定str开头，返回True/False
  ```
- ```python
  strip(str)		# 删除字符串两把的str代表的字符，如果不指定str则删除空白字符
  # 举例
  print(t.strip('a'))		# '1234'
  
  rstrip()和lstrip()	#删除字符串右边或者左边的str
  ```

  

### 4、列表类型(List)

![](/home/kirk/Desktop/learn-code/level_14/5.png)



#### a.列表的常用函数

- ```python
  list.append(object)  # 在列表末尾添加新的对象
  # 举例
  list1 = ['hello', 'python', 'java', 'world']
  list1.append('x')
  print(list1)	# ['hello', 'python', 'java', 'world', 'x']
  ```

- ```python
  list.count(object)  # 统计某个元素在列表中出现的个数
  # 举例
  print(list1.count('java'))	# 1
  ```

- ```python
  list.extend(seq)  # 在列表末尾一次性追加另一个序列的多个值(用新列表扩展原来的列表)
  # 举例
  list2 = ['x']
  list1.extend(list2)		# ['hello', 'python', 'java', 'world', 'x']
  ```

- ```python
  list.index(object)  # 从列表中找出某个值第一个匹配项的索引位置，索引从0开始
  # 举例
  print(list1.index('java'))	# 2
  ```

- ```python
  list.insert(index, object)  # 将对象插入列表某个索引位置
  # 举例
  list1.insert(0, list2)	# [['x'], 'hello', 'python', 'java', 'world']
  ```

- ```python
  list.pop(index)  # 移除列表中的一个元素(默认最后一个元素),并且返回该元素的值
  # 举例
  print(list1.pop(0))		# hello
  print(list1)		# ['python', 'java', 'world']
  ```

- ```python
  list.remove(object)  # 移除列表中某个值的第一个匹配项
  # 举例
  list1.remove('java')	# ['hello', 'python', 'world']
  ```

- ```python
  list.reverse()  # 反向列表中的元素
  # 举例
  list1.reverse()		# ['world', 'java', 'python', 'hello']
  ```

- ```python
  list.sort()  # 对原列表进行排序(无返回值)
  # 举例
  list1.sort()	# ['hello', 'java', 'python', 'world']
  list1.sort(reverse=True)	# ['world', 'python', 'java', 'hello']
  ```

- ```python
  list.copy()		# 复制一个列表
  # 举例
  list3 = list1.copy()
  ```

- ```python
  list.clear() # 清楚列表中所有元素
  # 举例
  list1.clear()	# []
  ```

- ```python
  max(list)  # 求列表的最大值
  # 举例
  list4 = [1, 3, 4, 66, 2, 4, 5]
  print(max(list4))	# 66
  ```

- ```python
  min(list)  # 求列表最小值
  # 举例
  print(min(list4))	# 1
  ```

- ```python
  sum(list)  # 求列表的和
  # 举例
  print(sum(list4))	# 85
  ```

- ```python
  len(list)  # 求列表中元素个数
  # 举例
  print(len(list4))	# 7
  ```

- ```python
  list(str)  # 将字符串强制转换为列表
  # 举例
  s = 'java'
  print(list(s))	# ['j', 'a', 'v', 'a']
  ```

- ```python
  list(range(start, end))  # 快速生成指定范围内数字列表
  # 举例
  print(list(range(1,10)))	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```



### 5、元组类型(Tuple)

![](/home/kirk/Desktop/learn-code/level_14/6.png)

#### a.如果元组只有一个元素的话，必须在这个元素后面加一个逗号，才会定义为一个元组对象

```python
a = ('hello',)		# tuple
b = ('hello')		# string
print(type(a), type(b))
```

#### b.元组常用方法

- ```python
  len(tuple)	# 计算元组元素个数
  ```

- ```python
  max(tuple)	# 返回数字元组最大值
  ```

- ```python
  min(tuple)	# 返回数字元组最小值
  ```

- ```python
  tuple(seq)	# 将列表转换为元组
  ```

  

### 6、 集合类型(Set)

#### a.集合的特性: 

##### 		1.无序不重复，主要用于消除重复元素

##### 		2.集合没有下标(index)

#### b.如何创建一个集合？

##### 	1. 使用花括号 如： s={1,2,3,5,6}	

##### 	2.使用set()函数 如：s1 = set{[2,3,5,6,7]}

#### c.将字符串'hello world！'转换为集合？

```python
print(set('hello world!'))		# {' ', 'l', 'w', '!', 'o', 'r', 'd', 'e', 'h'}
```

#### d.集合常用函数

- ```python
  s ={'x','1'}
  s.add(12)	# 添加一个元素12
  ```

- ```python
  s.remove('x')	# 删除一个元素'x'
  ```

- ```python
  del(s)		# 删除整个集合
  ```

- ```python
  s.clear()	# 清空集合
  ```

- ```python
  len(s)		# 集合长度计算
  ```

- ```python
  print('x' in s)		# 判断集合是否有某元素‘x’ 有则返回True，无则返回False
  ```

- ```python
  for _ in s:
      print(_)	# 输出集合中所有元素
  ```



### 7、 字典类型(Dictionary)

![](/home/kirk/Desktop/learn-code/level_14/7.png)

#### a.字典的特性

##### 1.无序

##### 2.由键值对组成的项，不同的项由逗号分隔

##### 3.键不可重复，可以通过键取得对应的值，值可以重复

#### b.字典的常用方法

- ```python
  dict.clear()	# 删除字典内所有元素
  # 举例
  dic1 = {'name': 'fy', 'age': 1}
  dic1.clear()
  print(dic1)		# {}
  ```
  
- ```python
  dict.copy()		# 返回一个字典的深复制
  # 举例
  dic2 = dic1.copy()
  dic2['name'] = 'wn'
  print(dic1)		# {'name': 'fy', 'age': 1}
  print(dic2)		# {'name': 'wn', 'age': 1}
  ```

- ```python
  dict.fromkeys([])		# 创建一个以序列[]中的元素作为键的新字典，默认键值为None
  # 举例
  mydic = dict.fromkeys(['name', 'age', 'id'])
  print(mydic)	# {'name': None, 'age': None, 'id': None}
  ```
- ```python
  dict.get(key,default=None)		# 返回指定键的值，如果键不在字典中返回default值
  # 举例
  print(dic1.get('id'))	# None
  print(dic1['id'])		# 会报错KeyError
  ```
- ```python
  dict.update(dict2)		# 把字典dict2的键值对更新到dict中
  # 举例
  dic1.update({'y': 2, }, x=1, )
  print(dic1)		# {'name': 'fy', 'age': 1, 'y': 2, 'x': 1}
  ```
- ```python
  dict.keys()		# 以列表返回一个字典所有的键
  # 举例
  print(dic1.keys())	# dict_keys(['name', 'age'])
  ```
- ```python
  dict.values()	# 以列表返回一个字典所有的值
  # 举例
  print(dic1.values())	# dict_values(['fy', 1])
  ```
- ```python
  dict.items()	# 返回字典中的键值对列表
  # 举例
  print(dic1.items())		# dict_items([('name', 'fy'), ('age', 1)])
  ```
- ```python
  dict.popitem()	# 随机删除列表中的任意一项
  # 举例
  print(dic1.popitem())	# ('age', 1)	# 以元组形式随机删除一组键值对
  print(dic1)				# {'name': 'fy'} 
  ```
- ```python
  dict.pop(key)	# 删除指定的键值对
  # 举例
  print(dic1.pop('age'))		# 1	# 返回删除的键的值
  print(dic1)					# {'name': 'fy'}
  ```



## 三、控制结构------判定结构和循环结构

### 1、分支结构常用比较运算符

```python
if a > b	# 大于号
if a <= b	# 小于等于号
if a == b	# 等等号（相等时为真）
if a != b	# 不等号
if a:		# 当a为真时条件成立，等价于 if a == True
if not a:   # 当a为假时条件成立，等价于 if a == False
```

- 在Python中会被认为是False的值： None、[]、""、0、{}、()



### 2、While循环

![](/home/kirk/Desktop/learn-code/level_14/8.png)

### 3、For循环

![](/home/kirk/Desktop/learn-code/level_14/9.png)

## 四、Python 函数

### 1、函数的意义

![image-20220320191803491](/home/kirk/.config/Typora/typora-user-images/image-20220320191803491.png)



### 2、函数的定义

![image-20220320191853584](/home/kirk/.config/Typora/typora-user-images/image-20220320191853584.png)

### 3、函数的定义规则

![image-20220320192013851](/home/kirk/.config/Typora/typora-user-images/image-20220320192013851.png)

### 4、函数参数

![image-20220320192051302](/home/kirk/.config/Typora/typora-user-images/image-20220320192051302.png)

#### a.函数参数---位置参数(Positional Argument)

![image-20220320192242488](/home/kirk/.config/Typora/typora-user-images/image-20220320192242488.png)



#### b.函数参数---关键字参数

![image-20220320192329914](/home/kirk/.config/Typora/typora-user-images/image-20220320192329914.png)



#### c.函数参数---默认值参数

![image-20220320192420699](/home/kirk/.config/Typora/typora-user-images/image-20220320192420699.png)

#### d.函数参数---不定长参数(元组--*args)

![image-20220320193509421](/home/kirk/.config/Typora/typora-user-images/image-20220320193509421.png)

- ##### 范例

  ```python
  def printinfo(argc, *args):
      print("This:", argc)
      for var in args:
          print(var)
      print(type(args))
      return
  
  
  printinfo(4)		# This: 4
  printinfo(7, 'woniu', 20, 21)	# This: 7 
  								# woniu 20 21	<class 'tuple'>
  lst = [1, 2, 3, 4, 5]
  printinfo(1, *lst)		# lst前面的*号代表自动解包lst这个列表，让lst中每个元素都作为函数参数
  # This: 1  1 2 3 4 5---->带*号解包lst传入
  printinfo(1, lst)		# This: 1   [1, 2, 3, 4, 5] --->不带*号传入整个lst
  ```

  

#### e.函数参数---不定长参数(字典---**kwargs)

![image-20220321084230546](/home/kirk/.config/Typora/typora-user-images/image-20220321084230546.png)

- ##### PS: 注意，不定长参数需要写在位置参数的后面，否则会报错

- ``` python
  范例
  def printinfo(argc, **kwargs):
      print("This:", argc)
      for k, v in kwargs.items():
          print(k, ':', v)
      print(type(kwargs))
      return
  
  
  printinfo(1, a='1', b=3)		# 正确
  """
  This: 1
  a : 1
  b : 3
  """
  
  printinfo(a='1', b=3, 1)		# 报错
  # SyntaxError: positional argument follows keyword argument
  ```

  
### 5、函数变量作用域

   ![image-20220321085015213](/home/kirk/.config/Typora/typora-user-images/image-20220321085015213.png)

#### a. 一个变量必须先初始化再访问，不能先访问再初始化

```python
print(b)
b = 1		# 报错	NameError: name 'b' is not defined
```

#### b. 全局变量使用规则

![image-20220321085437020](/home/kirk/.config/Typora/typora-user-images/image-20220321085437020.png)

- ```python
  b = 1
  lst = [1, 2]
  
  
  def func():
      a = 0
      # global b  # 声明当前使用的变量b是全局变量，请不要创建同名的局部变量
      # b = 10    # 如果没有global声明， 则相当于在函数内定义了一个与全局变量同名的局部变量
      global lst
      lst = ['a', 'b']	# 通过 ‘=’ 赋值号改变全局变量的值时，需要global声明
      # lst.append(3)		# 通过append函数为lst增加元素时，不需要global声明
      print(lst)
      print(a)
  
  
  func()
  print(lst)
  
  # 输出结果为
  """
  ['a', 'b']	# 函数内部输出lst
  0			# 函数内部输出a
  ['a', 'b']	# 函数外输出全局变量lst
  """
  ```





