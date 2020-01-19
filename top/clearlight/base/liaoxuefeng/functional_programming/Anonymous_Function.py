# 匿名函数

# 关键字lambda表示匿名函数, 冒号前面的x: 函数参数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8])))

f = lambda x: x * x
# 匿名函数也是一个函数对象
print(f)
print(f(5))


# 匿名函数也可以作为返回值返回
def build(x, y):
    return lambda: x * x + y * y


print(build(3, 2)())


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)

# 将上面函数改造成匿名函数
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
