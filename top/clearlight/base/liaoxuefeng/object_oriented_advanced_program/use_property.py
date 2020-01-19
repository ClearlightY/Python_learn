from builtins import print

'''
@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，
这样，程序运行时就减少了出错的可能性。
'''


class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

    # birth是可读写属性
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # age是一个只读属性
    @property
    def age(self):
        return 2015 - self._birth


s = Student()
s.set_score(60)
print(s.get_score())

# s.set_score(9999)

s1 = Student()
# 实际转化为s.set_score(60)
s.score = 60
print(s.score)

# @property属性的赋值方式
s1.birth = 1992
print(s1.birth)
print(s1.age)


# ValueError: score must between 0~100!
# s.score = 9999


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
