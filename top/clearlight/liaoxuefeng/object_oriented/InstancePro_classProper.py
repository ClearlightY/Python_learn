# 实例属性和类属性


class Student(object):
    # 类属性
    name = 'Student'

    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90
print(s.score, s.name)


class Stu(object):
    name = 'Student'


s = Stu()
print(s.name)
print(Stu.name)
# 给实例绑定name属性
s.name = 'Michael'
# 由于实例属性优先级比类属性高, 因此, 它会屏蔽掉类的name属性
print(s.name)
# 但是类属性并未消失, 因此, 它会屏蔽掉name属性
print(Stu.name)

# 如果删除实例的name属性
del s.name
# 再次调用s.name, 由于实例的name属性没有找到, 类的name属性就显示出来了
print(s.name)


# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。


# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# s1 = Student('Lisa')
# print(s1.count)
# s2 = Student('Mike')
# print(s2.count)

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


'''
实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''