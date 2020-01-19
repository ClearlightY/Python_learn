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
L = [1, 2, 3, 8, 3, 2, 1]
a = range(100)
print(a)
s1 = L[:len(L) // 2]
s2 = L[-(len(L) // 2):]
s2_num = len(s2) - 1
for s in s1:
    if s != s2[s2_num]:
        print('不相等')
    s2_num -= 1
    print(s)

L = range(10)
print(L)
print(list(L))


# def is_palindrome(m):
#     n = str(m)
#     s2_num = len(n) - 1
#     s1 = n[:len(n) // 2]
#     s2 = n[-(len(n) // 2):]
#     s2_num = len(s2) - 1
#     L = []
#     for s in s1:
#         if s != s2[s2_num]:
#             continue
#         s2_num -= 1
#         L.append(s)
#         print(L)


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

s = '123'
print(s[:2])


def is_palindrome(s):
    s = str(s)

    return s == s[::-1]


def main():
    output = filter(is_palindrome, range(1, 1000))

    print(list(output))


if __name__ == '__main__':
    main()
