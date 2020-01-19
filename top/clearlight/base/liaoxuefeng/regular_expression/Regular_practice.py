import re

'''

匹配边长的字符
.: 任意字符, 可以匹配任何单个字符
*: 任意个字符
+: 至少一个字符
{n}: 表示n个字符
{n,m}: 表示n-m个字符

精确匹配:
\d: 匹配一个数字
\w: 匹配一个数字或字母

[]: 表示范围
更精确的匹配:
[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，
                        也就是Python合法的变量；

[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

|:或
^:表示行的开头
$:表示行的结束

\d{3}: 匹配3个数字
\s: 匹配一个空格(也包括Tab等空白符)
'''

# 正则表达式的练习
s = 'ABC\\-001'
print(s)

# r前缀: 就不用考虑转义的问题了
s = r'ABC\-001'
print(s)

# 判断正则表达式是否匹配
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

print(re.match(r'^\d{3}\s\d{3,8}$', '010 12345'))

# 常见的判断方法:
test = '用户输入的字符串'
# if re.match(r'正则表达式', test):
if re.match(r'\d{8}', test):
    print('ok')
else:
    print('failed')

# 切分字符串
print('a b  c'.split(' '))
print('a , b  c'.split(' '))
# 无论多少空格, 都可以分割
print(re.split(r'\s+', 'a b  c'))
print(re.split(r'[\s\,]+', 'a,, b  c'))
print(re.split(r'[\s\,\;\`]+', 'a,b ;`;c d``e'))

# 分组
# ()表示的就是要提取的分组(Group)
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group())
# group(0)永远是原始字符串, group(1),group(2)..表示第1,2...个子串
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.group(3))

# 贪婪匹配
# 正则匹配默认是贪婪匹配, 也就是尽可能多的字符
print(re.match(r'^(\d+)(0*)$', '102300').groups())
# ?可以让\d+采用非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8)$')


# 使用
# print(re_telephone.match('010-12345').groups())
# print(re_telephone.match('010-4324').groups())

def is_valid_email(addr):
    if re.match(r'^[0-9a-zA-Z.]+@(\w+).com$', addr):
        return True


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


def name_of_email(addr):
    if re.match(r'^<(.+)>', addr):
        q = re.compile(r'^<(.+)>', re.M)
        return q.match(addr).groups()[0]
    p = re.compile(r'(.*)@', re.M)
    return p.match(addr).groups()[0]


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
