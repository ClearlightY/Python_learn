def mye(level):
    if level < 1:
        raise Exception("Invalid level!")
        # 触发异常后，后面的代码就不会再执行


try:
    mye(0)  # 触发异常
except Exception as err:
    print(1, err)
else:
    print(2)
