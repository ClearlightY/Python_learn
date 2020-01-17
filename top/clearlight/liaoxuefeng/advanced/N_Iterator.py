from collections.abc import Iterable, Iterator

# 迭代器

# Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# Iterator: 可以被next()函数调用并不断返回下一个值的对象成为迭代器
print('Iterator')
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('abc'), Iterator))



