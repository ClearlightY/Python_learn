def c2f(cel):
    fah = cel * 1.8 + 32
    return fah


def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel


def test():
    print("22摄氏度 = %.2f华氏度" % c2f(22))
    print("0华氏度 = %.2f摄氏度" % f2c(0))


if __name__ == '__main__':
    test()


# print(__name__)
