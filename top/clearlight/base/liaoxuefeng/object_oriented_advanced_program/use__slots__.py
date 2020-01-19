from types import MethodType

# 使用__slots__

'''
限制实例的属性: Python允许在定义class的时候, 定义一个特殊的__slots__变量来限制该class实例能添加的属性

注意:
    __slots__定义的属性仅对当前类实例起作用, 对继承的子类是不起作用的
    
__slots__限制的是实例属性的添加，不限制类属性添加
'''


class Student(object):
    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age')
    pass


'''
s = Student()
# 动态给实例绑定一个属性
s.name = 'Michael'
print(s.name)


# 给实例绑定一个方法
def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


# 给实例绑定一个方法
s.set_agea = MethodType(set_age, s)
s.set_agea(25)
print(s.age)


# 给一个实例绑定的方法, 对另一个实例是不起作用的
# 给class绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(100)
print(s.score)

s2 = Student()
s2.set_score(200)
print(s2.score)
'''

# 创建新的实例
s = Student()
# 绑定三个属性
s.name = 'Michael'
s.age = 25


# AttributeError: 'Student' object has no attribute 'score'
# s.score = 99

# 继承的子类不起作用
class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 9999
print(g.score)