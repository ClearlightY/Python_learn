# 高阶函数: filter() : 过滤序列

# 一个list中, 删掉偶数, 只保留奇数
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 3, 4233])))


# 把一个序列中的空字符删掉
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))
print(' s ' and 's'.strip())
print(' s ')


# 埃氏筛法
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 测试切片
L = [1, 2, 3, 2, 1]
print(L[:len(L) // 2])
print(L[-(len(L) // 2):])
a = range(100)
print(a)


def is_palindrome(n):
    pass
