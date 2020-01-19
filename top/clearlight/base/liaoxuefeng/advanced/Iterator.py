from collections.abc import Iterable

# 高级特性: 迭代

# 无论有无下标, 都可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
# 迭代字典的key
for key in d:
    print(key)

# 迭代字典的value
for value in d.values():
    print(value)

# 同时迭代字典的key和value
for k, v in d.items():
    print(k, ':', v)

# 迭代字符串
for ch in 'ABCD':
    print(ch)

# 如何判断一个对象是可迭代对象呢?
# 方法是通过collections模块的Iterable类型判断
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# Python内置的enumerate函数: 可以把一个list编程索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# for循环中, 同时引用两个变量
for x, y in [(1, 2), (2, 4), (3, 9)]:
    print(x, y)


# 用迭代查找一个list中最小和最大值
def findMinAndMax(L):
    M = (None, None)
    if len(L) != 0:
        min = L[0]
        max = L[0]
        for x in L:
            if min > x:
                min = x
            if max < x:
                max = x
        M = (min, max)
    return M


print(findMinAndMax([7, 1]))
print(findMinAndMax([]))

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 强化训练
for x in iter([1, 2, 3, 4]):
    print(x)

it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


