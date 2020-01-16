# 高级特性: 切片
L = ['Mike', 'Jerry', 'Bob', 'Luck']

# 1
print([L[0], L[1]])

# 2. 循环
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

print(L)
# 3. 切片
print('切片')
print(L[0:3])
print(L[:3])
print(L[1:3])
# 倒数第一个元素的索引是 -1
print(L[-2:])
# 取出倒数第二个元素
print(L[-2:-1])
# 取出最后一个元素
print(L[-1:])

L = list(range(100))
print(L)

print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])
print(L[:])
print((0, 1, 2, 3, 4, 5)[:3])
print('abcdefg'[:3])
print('abcdefg'[::2])
print(L[1:])


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，
# 注意不要调用str的strip()方法：
def trim(s):
    while s[:1] == ' ' or s[-1:] == ' ':
        if s[:1] == ' ':
            s = s[1:]
        elif s[-1:] == ' ':
            s = s[:-1]
    return s


print(trim(' hello'))
print(trim('  hello  '))
print(trim('  '))
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')