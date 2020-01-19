# 多重继承

'''
通过多重继承, 一个子类就可以同时获得多个父类的功能
'''


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Carnivorous(object):
    def eat(self):
        print('eat meat...')


# 多重继承
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class RunnableMixIn(Runnable):
    pass


class CarnivorousMixIn(Carnivorous):
    pass


# MixIn
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass

# MixIn的目的就是给一个类增加多个功能, 这样, 在设计类的时候,
# 我们优先考虑多重继承来组合多个MixIn的功能, 而不是设计多层次的复杂的继承关系

