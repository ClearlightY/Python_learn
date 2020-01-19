import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-12))


# 空函数
def nop():
    # pass: 作为占位符, 先让代码可以运行起来
    pass


# isinstance(): 数据类型检查
def m_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# print(m_abs('A'))


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 分别用一个, 两个参数来接受返回值
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)


# 求二元一次方程的方法, 不严谨
def quadratic(a, b, c):
    x = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    y = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x, y


def new_quadratic(a, b, c):
    val = b ** 2 - 4 * a * c
    if a == 0:
        print('方程式不成立, a不能等于0')
    elif val < 0:
        print('该方程无解')
    else:
        x1 = (-b + math.sqrt(val)) / (2 * a)
        x2 = (-b - math.sqrt(val)) / (2 * a)
        return x1, x2




# 测试:
print('new_quadratic(2, 3, 1) =', new_quadratic(2, 3, 1))
print('new_quadratic(1, 3, -4) =', new_quadratic(1, 3, -4))

if new_quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif new_quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

