def write_msg():
    filename = 'programming.txt'
    with open(filename, 'w') as file_obj:
        file_obj.write("python good")


def append_write_msg():
    filename = 'programming.txt'
    with open(filename, 'a') as file_obj:
        file_obj.write("\nI think it is simple by use")


if __name__ == '__main__':
    # write_msg()
    append_write_msg()