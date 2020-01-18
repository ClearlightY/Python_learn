# 访问限制

class Student(object):
    # 私有变量: 属性名称前加两个下划线__. 只有内部可以访问, 稳步不能访问
    # 一个下划线_开头的实例变量名: 这样的实例变量外部是可以访问的, 但是规定'虽然可以被访问,
    #                           但请把它视为私有变量, 不能随意访问
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s : %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


if __name__ == '__main__':
    lisa = Student('Lisa', 43)
    print(lisa.get_name())
    lisa.print_score()
    # print(lisa.__name)
    # 设置分数
    lisa.set_score(89)
    lisa.print_score()
    # Python解释器把__name变量改成了_Student__name
    print(lisa._Student__name)
    print(lisa._Student__score)


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


