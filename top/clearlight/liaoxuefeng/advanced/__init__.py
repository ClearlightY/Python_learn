import math


# 此py是认识py的main的第一步! 类似Java一样的主函数一样.
# if __name__ == '__main__':


def create_list():
    list = []

    n = 1

    while n <= 99:
        list.append(n)

        n += 2

    print(list)


def main():
    # create_list()

    arr = list(range(1, 100, 2))

    print(arr)


if __name__ == '__main__':
    main()
