import django
text = 'This is my first txt,\nThis is a new line.\nThis is last time'
print(text)

text = '''This is my first txt,
This is a new line,
This is last time.
'''
print(text)

append_text = '\nThis is appended file'

# 新建一个文件, 并写入text的内容
# open函数的参数:
# 第一个是文件
# 第二个: w - 写  a - 文本末尾追加
my_file = open('myfile.txt', 'w')
my_file.write(text)
my_file.close()

my_file = open('myfile.txt', 'a')
my_file.write(append_text)
my_file.close()

# 读取文件
file = open('myfile.txt', 'r')
content = file.read()
print(content)
file.close()

# 逐行读取
file = open('myfile.txt', 'r')
print('逐行读取')
content = file.readline()
second_read_time = file.readline()
print(content, second_read_time)
file.close()

file = open('myfile.txt', 'r')
content = file.readlines()
print(content)
file.close()

