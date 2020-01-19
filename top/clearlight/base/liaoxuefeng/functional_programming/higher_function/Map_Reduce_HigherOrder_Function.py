from functools import reduce

# 高阶函数: map/reduce

# 变量可以指向函数
print(abs(-10))
print(abs)

x = abs(-10)
print(x)

# 变量指向函数
x = abs
print(x)

# 变量指向abs函数本身. 直接调用abs()函数和调用变量x()完全相似
print(x(-19))


# 函数参数传入函数
def add(x, y, f):
    return f(x) + f(y)


# 一个函数能够把其它函数作为参数使用，这个函数就是高阶函数。
print(add(-5, 6, abs))


# map/reduce

# map()函数: 接受两个参数, 一个是函数, 一个是Iterable(可作用于for循环的对象)
# 作用: map将传入的函数一次作用到序列的每个元素, 并把结果作为新的Iterator返回
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
# 由于结果r是一个Iterator
# Iterator是惰性序列, 因此通过list()函数让它把整个序列都计算出来并返回一个list
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# reduce:把一个函数作用在一个序列, 接受两个参数, reduce把结果继续和序列的下一个元素做累积计算
# 序列求和, 用reduce实现
def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


# 把序列[1,3,5,7,9]变成13579
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# 把str转换为int的函数
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))

# 上面两个函数整理成一个函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2int('13579'))

# lambda函数进一步简化
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('13579'))


# 1. 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return str.lower(name).capitalize()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 2.Python提供的sum()函数可以接受一个list并求和
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 3.利用map和reduce编写一个str2float函数
# 把字符串'123.456'转换成浮点数123.456
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}


def str2float(s):
    flag = len(s) - s.index('.') - 1

    def charTonum(s):
        return DIGITS[s]

    for i in range(len(s)):
        if s[i] == '.':
            s1 = s[:i]
            s2 = s[i + 1:]

    def f(x, y):
        return x * 10 + y

    return reduce(lambda x, y: x * 10 + y, map(charTonum, s)) / 10 ** flag


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
