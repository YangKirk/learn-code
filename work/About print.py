#浮点数用e表示科学计数法的10;16进制数用0x前缀和0-9，a-f表示
print(1.23e9,'\n',1.2e-5,'\n',0xff00,'\n',0xa5b4c3d2)
#字符串可以用\来标识既有"又有'的情况,而如果'本身也是一个字符可以用""括起来
print('I\'m\"OK\"!','\n',"I'm OK，Thank you！")
#\\表示输出\字符
print('\n\\\t\\\t\\\t\\')
#\n是换行字符，\t是制表符
print('I\tLove\tYou\tVV\n')
#r可以让''内部字符串不转义,
print(r'\n''\\\t\\\t\\\t\\')
#'''xxx'''是多行输入字符
print('''line1
line2
line3
\\''')
