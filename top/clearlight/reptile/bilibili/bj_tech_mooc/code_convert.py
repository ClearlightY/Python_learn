f_path = 'F://wmz/article_info_660000_730000.json'
f_content = 'F://wmz/article_info_660000_730000_right.json'
f = open(f_content, 'a', encoding='utf-8')
with open(f_path, 'r', encoding='utf-8', errors='ignore') as fr:
    for line in fr.readlines():
        f.write(line)
    # f.write(fr.read())

fr.close()
f.close()


