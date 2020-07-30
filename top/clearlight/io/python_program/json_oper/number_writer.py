import json


def number_writer():
    numbers = [2, 3, 5, 2, 1, 4]

    filename = 'numbers.json'
    with open(filename, 'w') as f_obj:
        json.dump(numbers, f_obj)


def number_reader():
    filename = 'numbers.json'
    with open(filename) as f_obj:
        numbers = json.load(f_obj)

    print(numbers)


def remember_me():
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you com back, " + username + "!")


def greet_user():
    filename = 'username.json'
    with open(filename) as f_obj:
        username = json.load(f_obj)
        print("Welcome back, " + username + "!")


def remember_me_2():
    # 如果以前存储了用户名, 就加载它
    # 否则, 就提示用户输入用户名, 并存储它
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")


if __name__ == '__main__':
    # number_writer()
    # number_reader()
    # remember_me()
    # greet_user()
    remember_me_2()
