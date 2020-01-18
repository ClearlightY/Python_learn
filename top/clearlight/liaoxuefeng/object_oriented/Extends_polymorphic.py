# 继承和多态

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
# 子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写

# 定义一个class的时候, 我们实际上就定义了一种数据类型
class Animal(object):
    def run(self):
        print('Animal is running...')

    def eat(self):
        print('Eating meat...')


class Dog(Animal):
    # 重写方法
    # def run(self):
    #     print('Dog is running')

    pass


class Cat(Animal):
    def run(self):
        print('Cat is running')

    pass


# 继承的好处: 子类获得了父类的全部功能.
dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
# Dog是Animal的子类
print(isinstance(c, Animal))


# 运用多态, 具体调用的run方法, 由运行时该对象的确切类型决定, 这就是多态真正的威力
def run_twice(animal):
    animal.run()
    animal.run()


# 方法调用类，只是有相同方法的名字就可以调用
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

print(type(b))
print(type(a))
print(type(c))