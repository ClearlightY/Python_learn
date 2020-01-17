# 返回函数


# 普通函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax


# 函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


print(calc_sum(*[1, 2, 3]))
print(lazy_sum(12, 12)())

f1 = lazy_sum(1, 3, 5)
f2 = lazy_sum(1, 3, 5)
print(f1 == f2)
print(f1() == f2())


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# fix:
def count():
    fs = []

    def f(n):
        def j():
            return n * n

        return j

    for i in range(1, 4):
        fs.append(f(i))

    # print(list(fs))
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


