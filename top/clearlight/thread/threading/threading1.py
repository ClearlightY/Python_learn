import threading


def thread_job():
    print("This is an added Thread, number is %s" % threading.current_thread())
    # pass

def thread_job2():
    print("why only first thread")

def main():
    # 添加一个线程
    added_thread = threading.Thread(target=thread_job())
    added_thread2 = threading.Thread(target=thread_job2())
    added_thread2.start()
    added_thread.start()
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())


if __name__ == '__main__':
    main()
