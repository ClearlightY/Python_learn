import os

path = "F://testOSmkdir"

# 打开文件
fd = os.open(path+'//hello.txt', os.O_CREAT|os.O_RDWR)
# 写入字符串
line = "this is test"

# string needs to be converted byte object
b = str.encode(line)
ret = os.write(fd, b)

# ret constits of number of bytes written to hello.txt
print("the number of bytes written: ", ret)
# 关闭文件
os.close(fd)