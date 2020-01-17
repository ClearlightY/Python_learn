import sys
import math
import numpy

# import hello


print(sys.argv)
print(sys.argv, 'clearlight')

# print(hello.test())

# 作用域
'''
_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

导入模块的几种方式
1. import module1
2. from modname import name1
3. from modename import *
    把一个模块的所有内容全部导入到当前的命名空间
    

'''


# 私有函数
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


print(greeting('clearlight'))
print(greeting('cl'))

Money = 2000


# 我们在全局命名空间里定义一个变量 Money。
# 我们再在函数内给变量 Money 赋值，然后 Python 会假定 Money 是一个局部变量。
# 然而，我们并没有在访问前声明一个局部变量 Money，
# 结果就是会出现一个 UnboundLocalError 的错误。
def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1


print(Money)
AddMoney()
print(Money)

content = dir(math)
print(content)
print(dir(numpy))


