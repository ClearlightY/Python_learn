import json
import re
import traceback
import requests
from bs4 import BeautifulSoup


def get_html_text(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        }
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        # traceback.print_exc()
        return 200


def get_news_content(fpath, fcontent, fhistory_num):
    info_dict = {'url': '', 'title': '', 'content': '', 'class': '', 'tag': []}
    fh = open(fhistory_num, 'a', encoding='utf-8')
    fw = open(fcontent, 'a', encoding='utf-8')
    with open(fpath, 'r') as fr:
        print("注意:")
        # print("\t1. 直接回车将从第一行开始")
        print("\t1. 若异常结束,直接输入异常结束时的数字+1,即可继续爬取,")
        print("\t\t例如: 30行异常结束, 则输入31")
        print("\t2. 对于输出数据的文件, 是以追加形式写入文本, 故不用处理输出文本")
        print("\t3. F盘下有名字为: history_read_num.txt 的文件, 记录了已经打印的行数, 忘记了可以去看最后一条记录,从(最后一条记录+1)行开始即可")
        num = input("请输入想要开始的行号:")
        # if num == '\n\r' or num == '\r\n' or num == '\r' or num == '\n':
        # if num == '' or num == '\r\n' or num == '\r' or num == '\n':
        #     n = 0
        # else:
        n = int(num) - 1

        count = n
        # count = int(num)
        for line in fr.readlines()[n:]:
            # print(i)
            url = re.search(r'http.+\.html', line).group(0)
            print(url)
            count += 1
            # print(count)
            try:
                r = get_html_text(url)
                # 将url存入dict
                info_dict['url'] = url
                soup = BeautifulSoup(r, 'html.parser')
                # print(soup.prettify())
                nav = soup.find('nav')
                nav_a = nav.find_all('a')
                nav_con = '您现位置：'
                for nav_content in nav_a:
                    # print(nav_content.string)
                    nav_con += nav_content.string + '>'
                # print(nav_con + '>正文')
                # 导航存入dict
                info_dict['class'] = nav_con + '>正文'
                # print(nav)
                article = soup.find('article', attrs={'id': 'con_l'})
                # print(article)
                title = article.find('h1')
                # print(title.string)
                # 标题存入dict
                info_dict['title'] = str(title.string)
                section_tip = soup.find('section', attrs={'id': 'tip'})
                # print(section_tip)
                # print(article)
                tip = section_tip.find('h2')

                tag = tip.find_all('a')
                tag_con = []
                for t in tag:
                    tag_con.append(t.string)
                # 标签存到dict
                info_dict['tag'] = tag_con

                # 开始获取文章的内容
                # 文章有可能有多页, 因此需要爬取多个页面的内容
                web_url = re.search(r'http://www.cnwmz.com/html/\d+/\d+', line)
                content = ''
                for j in range(20):
                    # 尝试文章是否有多页, 若有多页的话, 则改变j的值进行内容添加
                    if j != 0:
                        j += 1
                        wu = str(web_url.group(0)) + '_' + str(j) + '.html'
                        wu_text = get_html_text(wu)
                        if wu_text == 200:
                            break
                        soup = BeautifulSoup(wu_text, 'html.parser')
                    article_content = soup.find('section', attrs={'id': 'article'})
                    for num, desc in enumerate(article_content.descendants):
                        dc = str(desc)
                        if str(desc.name) == 'a' or str(desc.name) == 'script' or dc == 'wm("arc");':
                            continue
                        if str(desc.name) == 'p' or str(desc.name) == 'br':
                            content += '\n'
                            continue
                        if re.match(r'[{p.*}上一页下一页<b>.*</b>]', dc):
                            continue
                        if dc == '1' or dc == '2' or dc == '3' or dc == '4' or dc == '5' or dc == '6':
                            continue
                        if dc == ' ':
                            continue
                        content += dc

                    # 文章内容存入dict
                # print(content)
                info_dict['content'] = content
                fw.write(json.dumps(info_dict, ensure_ascii=False) + '\n')
                fw.flush()
                fh.write(str(count) + '\n')
                fh.flush()
            except:
                traceback.print_exc()

            # fh.write(json.dumps(count, ensure_ascii=False) + '\n')
            print(count)
            # if i == 200:
            #     break
        # print(info_dict)
    fr.close()
    fh.close()
    fw.close()


def main():
    fhistory_num = 'F://wmz/history_read_num.txt'
    # flist_url = 'F://wmz/error_url_1.txt'
    # fcontent = "F://wmz/article_info_error_url.json"
    flist_url = 'F://wmz/500000_600000.txt'
    fname = re.search(r'\d+_\d+_?\d*_?\d*', flist_url)
    fcontent = "F://wmz/article_info_" + str(fname.group(0)) + ".json"
    # 获取想要的内容
    get_news_content(flist_url, fcontent, fhistory_num)


if __name__ == '__main__':
    main()
