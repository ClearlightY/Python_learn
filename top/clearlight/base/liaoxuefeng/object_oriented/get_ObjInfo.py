# 获取对象信息
import types

# 使用type()函数
from PyQt5.QtNetwork.QUdpSocket import readData

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

print(type(123) == type(456))
print(type(213) == int)
print(type('abc') == type(123))


def fn():
    pass


print(type(fn))
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 使用isinstance()
# 总是优先使用isinstance(): 判断类型，可以将指定类型及其子类“一网打尽”
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 使用dir()
print(dir('ABC'))

# __len__: 返回长度
# 实际上, len()函数内部: 自动去调用该对象的__len__()方法
print(len('ABC'))
print('ABC'.__len__())


# 实现len()函数
class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(obj)

# 测试对象的属性

# 判断有属性'x'
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
# 设置一个属性'y'
print(setattr(obj, 'y', 19))
# 判断是否有属性'y'
print(hasattr(obj, 'y'))
# 获取属性'y'
print(getattr(obj, 'y'))

print(obj.y)

# 可以传入一个default参数, 如果属性不存在, 就返回默认值
print(getattr(obj, 'z', 404))


# 获得对象的方法

# 判断有方法'power'
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
# 获取属性'power'并赋值到变量fn
# fn指向obj.power
fn = getattr(obj, 'power')
# 调用fn()与调用obj.power()是一样的
print(fn())


def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

