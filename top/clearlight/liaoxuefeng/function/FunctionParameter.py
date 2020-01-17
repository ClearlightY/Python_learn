# 位置参数
def power(x):
    return x * x


def n_power(x, n):
    return x ** n;


def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


# py不支持重载
# print(power(3))
print(power(3, 3))
print(n_power(3, 3))


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


# 当只提供一个参数时, 未提供的参数将为默认参数的值
print(power(5))


def enroll(name, gender, age=6, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# 不按顺序提供部分默认参数时, 需要把参数名写上
enroll('Bob', 'F')
enroll('Mike', 'M', 12)
enroll('Luck', 'G', city='nanjing')


# enroll('Pipe', 'F', 'hebei')


def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end(['x', 'y']))
print(add_end())
print(add_end())


# 定义默认参数要牢记一点: 默认参数必须指向不变对象!
# str: 不可变   list: 可变


# 参数为list或tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))


def chan_calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 利用可变参数调用函数
print(chan_calc(1, 2, 3))

# TypeError: can't multiply sequence by non-int of type 'list'
# print(chan_calc([1, 2, 3]))

print(chan_calc())

nums = [1, 2, 3]
print(chan_calc(nums[0], nums[1], nums[2]))
# 上面的写法太繁琐, 可以在list或tuple前面加一个*号
print(chan_calc(*nums))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Mary', 30)
# 关键字参数在函数内部自动组装为一个dict
person('Bob', 35, city='Beijing')
person('Adam', 20, gender='M', job='teacher', city='HuNan')

# 先祖装出一个dict, 再把该dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

# 复杂的调用简化形式
# kw获得的dict是extra的一份拷贝, 对kw的改动不会影响到函数外的extra
person('Jack', 35, **extra)


# 限制关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Jack', 24, city='Biejing', addr='Chaoyang', zipcode=2143)


# 命名关键字参数
# 需要一个特殊分隔符*, *后面的参数被视为命名关键字参数
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 调用方式
person('Jack', 24, city='Beijing', job='Engineer')
person('Mary', 18, job='teacher')


# 如果函数定义中已经有了一个可变参数, 后面跟着的命名关键字参数就不在需要一个特殊分隔符 * 了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person('Lucy', 18, (1, 2, 3), city='HeNan', job='teacher')
arg = [1, 2, 3]
person('Kit', 10, arg, city='Lundon', job='teacher')


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 函数调用的时候, Python解释器自动按照参数位置和参数名把对应的参数传进去
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 通过tuple或dict, 调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
f1(*args, **kw)


# def product(x, y):
#     return x * y


# 考虑不周到, 当参数长度为0时提示错误
# def product(*args):
#     x = 1
#     for num in args:
#         x = num * x
#     return x


# 修改版
def product(*args):
    if len(args) == 0:
        raise TypeError
    else:
        sum = 1
        for i in args:
            if not isinstance(i, (int, float)):
                raise TypeError
            else:
                sum *= i
    return sum



# print(my_product(5, 6, 7))

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
