def file_reader_1():
    # python在当前执行的文件所在的目录中查找指定的文件
    with open('test.txt', encoding='utf-8') as file_obj:
        contents = file_obj.read()
        print(contents.rstrip())  # rstrip()删除字符串末尾的空白


def file_reader_2():
    filename = r'test.txt'
    with open(filename, encoding='utf-8') as file_obj:
        for line in file_obj:  # 文件中每行的末尾都有一个看不见的换行符, 而print语句也会加上一个换行符
            print(line.rstrip())


def file_readlines_1():
    filename = r'test.txt'
    with open(filename, encoding='utf-8') as file_obj:
        lines = file_obj.readlines()

    for line in lines:
        print(line.rstrip())


def file_read_to_string():
    """将文件保存到字符串中"""
    filename = 'test.txt'
    with open(filename, encoding='utf-8') as file_obj:
        lines = file_obj.readlines()

    txt_string = ''
    for line in lines:
        txt_string += line.rstrip()

    print(txt_string)
    print(len(txt_string))


if __name__ == '__main__':
    # file_readlines_1()
    file_read_to_string()