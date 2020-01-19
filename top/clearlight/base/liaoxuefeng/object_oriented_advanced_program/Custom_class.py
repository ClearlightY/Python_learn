# 定制类

print()

'''
_xxx_的变量或者函数名:在Python中有特殊用途
'''


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student('Mike'))
s = Student('Luck')
