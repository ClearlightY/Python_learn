import re

# re.match: 从字符串的起始位置匹配一个模式, 如果不是起始位置匹配成功的话, match()就返回none

print()

'''
语法:
re.match(pattern, string, flags=0)
pattern: 匹配的正则表达式
string: 要匹配的字符串
flags: 标志位, 用于控制正则表达式的匹配方式, 如:是否区分大小写,多行匹配等

获取匹配表达式:
groups(): 返回一个包含所有小组字符串的元组, 从1到所含的小组号

re.search 扫描整个字符串并返回第一个成功的匹配。
函数语法：
re.search(pattern, string, flags=0)
'''

# 在起始位置匹配
print(re.match('www', 'www.runoob.com').span())
# 不在起始位置匹配
print(re.match('com', 'www.runoob.com'))

line = 'Cats are smarter than dogs?'
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print('matchObj.group():', matchObj.group())
    print('matchObj.group(1):', matchObj.group(1))
    print('matchObj.group(2):', matchObj.group(2))
else:
    print('No match!!')

print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span())

line = 'Cats are smarter than dogs?'
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print('searchObj.group():', searchObj.group())
    print('searchObj.group(1):', searchObj.group(1))
    print('searchObj.group(2):', searchObj.group(2))
else:
    print('Nothing found!!')

# compile函数
# 用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

# 用于匹配至少一个数字
pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four', 3, 10)
n = pattern.match('one12twothree34four', 2, 10)
print(m)
print(n)

print(m.group(0))
print(m.start(0))
print(m.end(0))
print(m.span(0))
