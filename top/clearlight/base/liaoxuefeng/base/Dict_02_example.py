def printWithChinese(dic):
    for i in dic:
        print(i, ":", dic[i])
    print('------------------')


book_dict = {"price": 500, "bookName": "Python设计", "weight": "250g"}

printWithChinese(book_dict)

book_dict["owner"] = "tyson"
# 第一种方式，指定key，并且为其赋值一个value，如果key存在，就是修改value，反之就添加一个Entry（key-value）

printWithChinese(book_dict)

book_dict.update({"country": "china"})
# 第二种方式，使用update方法,传入一个字典进去，如果key存在，就会覆盖掉原有的value，反之就是添加一个或多个Entry（key-value）进入
# 多个Entry（key-value）的情况，取决于你的字典里有多少个元素，哈哈，明白里吧（一个元素即一个Entry（key-value））

printWithChinese(book_dict)

book_dict.update(temp="无语中", help="帮助")
# 第三种方式，直接传一个以key为变量进去，如果存在同样是修改value，不存在，就是添加一个或多个Entry进去（关键字参数形式，取决于你传入了几个关键字参数进去）

printWithChinese(book_dict)

# 注意，字典中的Entry是无序的#
# 遍历字典的时候，与你的添加元素顺序，与你的访问顺序都无关，当你遍历字典的时候，如果刚好与你添加元素的顺序是一样的话，我只能告诉你这是个美丽的巧合而已，需要有序字典请看OrderDict#
