# 装饰器


def now():
    print('2020-1-17')


# print(now())
f = now
f()

# 函数对象的属性__name__, 可以拿到函数的名字
print(now.__name__)
print(f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper



