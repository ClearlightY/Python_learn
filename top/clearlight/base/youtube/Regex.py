# 简单匹配
import re

pattern1 = 'dog'
pattern2 = 'bird'
string = 'dog r2ns to eat'
print(pattern1 in string)
print(pattern2 in string)

print(re.search(pattern1, string))
print(re.search(pattern2, string))

print(re.search(r'r[0-9a-z]n', string))

# \d:匹配一个数字 等价于[0-9]
print(re.search(r'r\dn', 'run r3n'))
# \D:匹配任意非数字
print(re.search(r'r\Dn', 'run r3n'))

# \s:匹配空白字符 [\t\n\r\f\v]
print(re.search(r'r\sn', 'r\nn r4n'))
# \S:匹配非空字符
print(re.search(r'r\Sn', 'r\nn r4n'))

# \w:匹配字母数字及下划线 [a-zA-Z0-9_]
print(re.search(r'r\wn', 'r\nn r4n'))
# \W:匹配非字母数字及下划线
print(re.search(r'r\Wn', 'r\nn r4n'))

# \b:匹配一个单词边界, 也就是指单词和空格间的位置
print(re.search(r'\bruns\b', 'dog runs to eat'))
# \B:匹配非单词边界
print(re.search(r'\Bruns\B', 'dogrunsto eat'))

# \\:匹配 \
print(re.search(r"runs\\", "runs\ to me"))
# .匹配任意字符(除了换行符)
print(re.search(r'r.n', 'r-ns to me'))

# ^:匹配字符串的开头
print(re.search(r'^dog', 'dog runs to cat'))
# $:匹配字符串的末尾
print(re.search(r'cat$', 'dog runs to cat'))

# ?:可能发生, 也可能不发生
print(re.search(r'Mon(day)?', 'Monday'))
print(re.search(r'Mon(day)?', 'Mon'))

# multi-line: 多行匹配, 影响^和$
string = '''
dog runs to cat
I run to dog.
'''
print(re.search(r'^I', string))
print(re.search(r'^I', string, flags=re.M))

#  *: 出现0或多次, 匹配任意字符
# 下面的例子也就是 b出现0次或多次
print(re.search(r'ab*', 'a'))
print(re.search(r'ab*', 'abbbbbb'))

print("sign******")
# +: 出现1或多次, 至少一个字符
print(re.search(r'ab+', 'a'))
print(re.search(r'ab+', 'abbbbbb'))

# {n, m}: 出现n到m次
print(re.search(r'ab{2, 10}', 'a'))
print(re.search(r'ab{2,10}', 'abbbbb'))

# group
match = re.search(r'(\d+), Date: (.+)', 'ID: 021433, Date: Feb/12/2020')
print(match.group())
print(match.group(1))
print(match.group(2))

# group获取的别名: (?P<别名>regex)
match = re.search(r'(?P<id>\d+), Date: (?P<Date>.+)', 'ID: 021433, Date: Feb/12/2020')
print(match.group('id'))
print(match.group('Date'))

# findall寻找所有匹配
print(re.findall(r'r[ua]n', 'run ren ran'))
# |: or
print(re.findall(r'run|ran', 'rdn ren ran'))
# print(re.findall(r'r(u|a)n', 'rdn ren ran'))

# 替换
# re.sub() replace
print(re.sub(r'r[au]ns', 'catches', 'dog runs to cat'))

# 分裂
# re.split()
print(re.split(r'[,;\.]', 'a;b,c.d;e'))

# compile
compiled_re = re.compile(r'r[ua]n')
print(compiled_re.search("dog ran to cat"))