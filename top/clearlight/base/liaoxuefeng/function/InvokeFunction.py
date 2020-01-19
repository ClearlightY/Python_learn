from DefineFunction import my_abs

# 绝对值
print(abs(-100))
print(abs(12.21))

# 最大值
print(max(1, 2, 4, 0, -13, 12))

# 数据类型转换
print(int('123'))
print(int(12.23))
print(float('12.123'))
print(str(1.23))
print(str(100))
print('bool(1)', bool(1))
print(bool(0))
print(bool(-2))
print(bool(''))
print(bool(12))

# 可以把函数名赋给一个变量, 相当于给这个函数起了一个"别名"
a = abs
print(a(-12))

n1 = 255
print(hex(n1))
print(hex(1000))

# 调用已经定义的函数
print(my_abs(-12))