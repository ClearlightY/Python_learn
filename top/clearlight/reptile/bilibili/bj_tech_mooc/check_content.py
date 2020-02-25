import json

f_law_data = 'F://wmz/article_info_250000_400000_500000_600000.json'
# f_law_data = 'F://wmz/article_info_1_2.json'
f_lack_content = 'F://wmz/lack_content.json'
f_missing_text = 'F://wmz/missing_text_num.json'
f = open(f_lack_content, 'a', encoding='utf-8')
fm = open(f_missing_text, 'a', encoding='utf-8')
f.write(f_law_data + ':' + '\n')
fm.write(f_law_data + ':' + '\n')
count = 0
with open(f_law_data, "r", encoding='utf-8') as fr:
    num = input("请输入想要开始的行号:")
    n = int(num) - 1
    count = n

    for line in fr.readlines()[n:]:
        try:
            j = json.loads(line.strip())
            # law_list.append(j)
            # law_dict = j
            # print(j)
            count += 1
            if j['url'] == '' or j['title'] == '' or j['content'] == '' or j['class'] == '' or j['tag'] == '':
                f.write(line + str(count) + '\n')
                print(j)
            print(count)
        except:
            fm.write(str(count) + '\n')
            continue
    # print(law_dict)
    # if i == 5:
    #     break

fr.close()
f.close()
