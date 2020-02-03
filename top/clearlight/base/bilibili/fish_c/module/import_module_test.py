# import TemperatureConversion
import TemperatureConversion as tc
from TemperatureConversion import f2c
import sys
import timeit

# print("32摄氏度 = %.2f华氏度" % TemperatureConversion.c2f(32))
print("32摄氏度 = %.2f华氏度" % tc.c2f(32))

print("99华氏度 = %.2f摄氏度" % f2c(99))

print(tc.__name__)

print(sys.path)


# print(help(timeit))

def test():
    """Stupid test function"""
    L = [i for i in range(100)]


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))
