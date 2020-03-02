import math

print("{} {}".format("hello", "world"))
# hello world

print("{1}".format("hello", "world"))
# world

print("{1} {0} {0}".format("hello", "world"))
# world hello hello

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

print("网站名: {name}, 地址 {url}".format(name="clearlight", url="www.clearlight.top"))
# 网站名: clearlight, 地址 www.clearlight.top

'''
通过字典设置参数
可以用 ** 标志将这个字典以关键字参数的方式传入
'''
site = {"name": "clearlight", "url": "www.clearlight.top"}
print("网络名: {name}, 地址 {url}".format(**site))
# 网络名: clearlight, 地址 www.clearlight.top

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# 通过列表索引设置参数
my_list = ['clearlight', 'www.clearlight.top']
print("网络名: {0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的


# 网络名: clearlight, 地址 www.clearlight.top

class AssignValue(object):
    def __init__(self, value):
        self.value = value


my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

# {}里面的:前面的数字代表后面format的第几个参数
# {}里面的:后面的数字会限定该字段的最宽度
print('The value of PI is approximately {1:7.3f}.'.format(math.pi, 12.3538))
print('The value of PI is approximately {1:.3f}.'.format(math.pi, 12.3538))
print('The value of PI is approximately {1:6.3f}.'.format(math.pi, 12.3538))

# 数字格式化
print("{:.2f}".format(3.141592654))
print("{:#X}".format(123))

# 可以使用大括号{}来转义大括号
print("{} 对应的位置是 {{0}}".format("runoob"))
# runoob 对应的位置是 {0}


# {}里面的:后面的d代表以十进制进行显示
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))


