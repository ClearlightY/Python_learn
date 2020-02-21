import json

# dic = {}
# # 读取代码
# fr = open('F://wmz/article_info_all.txt', 'r', encoding='utf-8')
# dic = eval(fr.read())
# print(dic)
#
# # with open('F://wmz/article_info_all.txt', 'r', encoding='utf-8') as fr:
#     # for i, line in enumerate(fr):
#     #     js = json.dumps(line)
#     #     print(line)
#     #     print(js)
#     #     if i == 10:
#     #         break
#     # dic = json.loads(fr.read())
#     # print(dic)
#
# fr.close()

law_dict = {}
law_list = []
with open('F://wmz/article_info_all.txt', "r", encoding='utf-8') as fr:
    for i, line in enumerate(fr):
        j = json.loads(line.strip())
        # law_list.append(j)
        # law_dict = j
        law_dict[j['url']] = j
        if i == 5:
            break
# print(law_list)
print(law_dict)
print(law_dict['title'])
