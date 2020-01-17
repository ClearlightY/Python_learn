# 面向对象编程
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    pass

    # bart = Student()
    # print(bart)
    # print(Student)


def print_score(std):
    print('%s: %s' % (std.name, std.score))


bart = Student('Mike', 18)
print(bart.name)
print(bart.score)
print_score(bart)
bart.print_score()
print(bart.get_grade())
