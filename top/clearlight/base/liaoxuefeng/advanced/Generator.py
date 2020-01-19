# 高级特性: 生成器
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
# 通过next()函数获得generator的下一个返回值
print(next(g))
print(next(g))
# 直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

# 正确的调用方式: for循环(generator也是可迭代对象)
for n in g:
    print(n)


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# a, b = b, a + b
# 上面的等式相当于:
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]

print(fib(6))


# 如果一个函数定义中包含了yield关键字, 那么这个函数就不再是一个普通函数, 而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print('直接打印f')
f = fib(6)
print(f)
for x in fib(6):
    print(f)


# 定义一个generator, 依次返回数字1, 3, 5
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


# generator和函数的执行列成不一样.
# 函数: 遇到return语句或最后一行函数语句返回
# generator: 每次调用next的时候执行, 遇到yield语句返回, 再次执行时从上次返回的yield语句处继续执行

# 生成一个generator对象, 然后用next()函数不断获得下一个返回值
o = odd()
print(next(o))
print(next(o))
print(next(o))
# Traceback
#   StopIteration
# print(next(o))

# odd是generator, 执行过程中, 遇到yield就中断, 下次又继续执行.

# for循环调用generator时, 拿不到generator的return语句的返回值. 如果想要拿到返回值,
# 必须补货StopIteration错误, 返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def triangles():
    L = [1]
    yield L
    L = [1, 1]
    yield L
    while True:
        # L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]
        L = [L[i - 1] + L[i] for i in range(1, len(L))]
        L.insert(0, 1)
        L.append(1)
        yield L


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
