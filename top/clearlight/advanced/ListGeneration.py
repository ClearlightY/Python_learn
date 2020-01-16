import os

# 高级特性:列表生成式

# 生成列表
print(list(range(1, 11)))

# 循环
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 列表生成式: [要生成的元素 for循环 if判断]
print([x * x for x in range(1, 11)])
# for循环后面加if判断
print([x * x for x in range(1, 11) if x % 2 == 0])
# 使用两层循环, 生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])

# for循环遍历dict: 展示同时使用两个甚至多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 非字符串类型没有lower()方法
x = 'abc'
y = 123
print(isinstance(x, str))
print(isinstance(y, str))

# 添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')