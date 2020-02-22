def foo(num):
    print("starting...")
    while num < 10:
        num = num + 1
        yield num


# debug看运行顺序 即可
for n in foo(0):
    print(n)


def gen(n):
    for i in range(n):
        yield i ** 2


for i in gen(5):
    print(i, " ", end="")
