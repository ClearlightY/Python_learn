import re
import json

print('hello world')

# 输入且包含提示信息并赋值
# name = input('please input your name')
# print("hello", name)

a = -100
if a >= 0:
    print(a)
else:
    print(-a)

age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')

# 多行打印
print(r'''line1,\n
line2
line3''')

a = 123  # a是整数
print(a)
a = 'ABC'  # a变为字符串
print(a)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 地板除(只保留整数部分)
print(47 // 6)

a = len('adfdf')
print(a)

# 格式化
print('%2d-%02d' % (3, 1))
print('%.3f' % 3.1415926)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

s1 = 72
s2 = 85
r = (85 - 72) / 72 * 100
print(r)
print('%.1f%%' % r)

print('中文'.encode('gb2312'))

# encode()方法:str编码为指定的bytes
# decode()方法: bytes变为str
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

# re模块的演示
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

# ord()函数获取字符的整数表示, chr()函数把编码转换为对应的字符
print(chr(20013))
print(chr(ord('毅')))

classNames = ['jack', 'bob', 'mary']
print(classNames)

# 打印指定索引的值
print(classNames[0])
print(classNames[1])
print(classNames[2])
# 倒序访问列表元素
print(classNames[-1])
print(classNames[-2])

# 翻转列表
classNames.reverse()
print(classNames)

# 添加元素
classNames.append("luck")
print(classNames)

# 在指定索引后添加元素
classNames.insert(2, "lucy")
print(classNames)

# 截取列表中的值
print(classNames[1:3])

# 删除列表元素
del classNames[1]
print(classNames)

# 弹出顶元素
classNames.pop()
print(classNames)

# 计算列表的个数
print(len(classNames))

# Python列表脚本操作符: *
print(['Hi' * 4])

# 迭代
for x in classNames: print(x)

# 判断是否存在列表中
print('jack' in classNames)

# 统计某元素出现的次数
classNames.append('jack')
print('jack出现的次数:', classNames.count('jack'))

# remove方法移除列表中第一个匹配项
classNames.insert(3, "blue")
print(classNames)
classNames.remove('jack')
print(classNames)

# 对愿列表进行排序
list.sort(classNames)
print(classNames)

# 返回列表中的最大最小值
print(min(classNames))
print(max(classNames))

# 指定元素原因替换为其他元素
classNames[0] = 'kite'
print(classNames)

# 列表中元素的数据类型可以不同, 也可以列表中存在列表
s = ['python', 1, classNames, True]
print(s)
