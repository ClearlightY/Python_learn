# 读取键盘输入


# raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
from click._compat import raw_input

str = raw_input("请输入:")
print('你输入的内容是:', str)

str = input()