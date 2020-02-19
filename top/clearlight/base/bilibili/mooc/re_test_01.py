import re

# re.search: 在一个字符串中搜索匹配正则表达式的第一个位置
match = re.search(r'[1-9]\d{5}', 'BIT 100032 132103 12043')
if match:
    print(match.group(0))

print(match)

# re.match: 从一个字符串的开始位置起匹配正则表达式
match = re.match(r'[1-9]\d{5}', '123042BIT 100032 132103 12043')
if match:
    print(match.group(0))

# re.findall: 搜索字符串, 以列表类型返回全不能匹配的子串
match = re.findall(r'[1-9]\d{5}', '123042BIT 100032 SUV132103 12043')
if match:
    print(match)

# re.split: 将一个字符串按照正则表达式匹配结果进行分割, 返回列表类型.
match = re.split(r'[1-9]\d{5}', '123042BIT 100032 SUV132103 120413')
if match:
    print(match)
# 结果:['', 'BIT ', ' SUV', ' ', '']
# 结果分析: 123042符合,则字符串开头开始分割即'',
#     然后就是'BIT ', 100032符合,继续分割, ' SUV'
#   132103符合,分割' ', 120413符合,后面一个''(空字符串)

# maxsplit=1, 只匹配1个, 后面的字符串作为一个元素输出
match = re.split(r'[1-9]\d{5}', '123042BIT 100032 SUV132103 120413', maxsplit=1)
if match:
    print(match)

for match in re.finditer(r'[1-9]\d{5}', 'BIT102342 RSU293129'):
    if match:
        print(match.group(0))
        print(match)

print(re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT102435 TSU104394'))

print(re.compile(r'[1-9]\d{5}').sub(':zip', 'BIT102342 TSU129424'))

# match对象
m = re.search(r'[1-9]\d{5}', 'BID102832 TJK192425')
print(m.string)
print(m.re)
print(m.pos)
print(m.endpos)

print(m.group(0))
print(m.start())
print(m.end())
print(m.span())

match = re.search(r'PY.*N', 'PYKSJDFNN')
print(match.group(0))

split = re.compile('[ \t\u3000]*-+$')
s = split.match('  \t-a')
print(s)

word_pattern = re.compile(r'\w+$')
print(word_pattern.findall('This is a something'))

phone_num = re.compile(r'\w{5}\s')

word_pattern2 = re.compile(r'\b\w{5}\b')
print(word_pattern.findall('These are some phone numbers 915-555-1234...hello'))
print(word_pattern2.findall('These are some phone numbers 915-555-1234...hello'))

num = re.compile(r'\(?\d{3}[-.)]\d{3}[-.]\d{4}')