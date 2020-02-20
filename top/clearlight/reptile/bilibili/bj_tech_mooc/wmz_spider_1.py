import requests
import re
from bs4 import BeautifulSoup
import traceback
import json
import sys


def get_html_text(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return 200
        # traceback.print_exc()


def get_nav_addr(lst, web_url):
    url = get_html_text(web_url + '/html/wenmimap.html')
    soup = BeautifulSoup(url, "html.parser")
    link_list = soup.find_all('div', attrs={'class': 'list'})
    # print(link_list)
    # print(link_list[0])
    # print(type(link_list[0]))
    # 获取map中导航的所有链接
    for list in link_list:
        ul_list = list.find('ul')
        # print(ul_list)
        a = ul_list.find_all('a')
        for i in a:
            try:
                href = i.attrs['href']
                lst.append(href)
            except:
                traceback.print_exc()


def get_article_url(lst, web_url, path):
    fw = open(path, 'a', encoding='utf-8')
    nav_count = 0
    # 获取每个文章的链接
    for nav_link in lst:
        article_count = 0
        print(nav_link)
        max_list = 0
        min_list = 0
        url = get_html_text(web_url + nav_link)
        soup = BeautifulSoup(url, "html.parser")
        page = soup.find('h3', attrs={'class': 'list_page'})
        # print(page)
        # 判断是否该页面有内容
        if page is None:
            continue
        min_page = page.find_all('a', string="首页")
        max_page = page.find_all('a', string="尾页")
        min_num = re.search(r'\d{1,4}', str(min_page[0]))
        max_num = re.search(r'\d{1,4}', str(max_page[0]))
        # 当只有一页的时候, 有可能链接为 /index.html, 因此没有想要的页码
        if min_num:
            min_num1 = int(min_num.group(0))
        else:
            min_num1 = 1
        if max_num:
            max_num1 = int(max_num.group(0))
        else:
            max_num1 = 1
        # 获取最大的页数, 开始遍历每一页中的文章内容
        num = int(max(min_num1, max_num1))
        try:
            for i in range(num):
                r = get_html_text(web_url + nav_link + 'List_' + str(i + 1) + '.html')
                # url = web_url + nav_link + 'List_' + str(i + 1) + '.html'
                # 将"http://www.cnwmz.com/html/jiguandanwei_tag/gongqingtuan/List_27.html"等等写入文本
                # fw.write(json.dumps(url, ensure_ascii=False) + '\n')
                soup = BeautifulSoup(r, "html.parser")
                # 直接获取<dt>标签中的内容
                # article = soup.find("article", attrs={'id': 'list_l'})
                article = soup.find_all('dt', soup)
                for article_list in article:
                    a = article_list.find('a')
                    href = a.attrs['href']
                    article_url = web_url + href
                    # print(article_url)
                    article_count += 1
                    fw.write(json.dumps(article_url, ensure_ascii=False) + '\n')
                    # print(href)
                    # lst.append(href)
                nav_count += 1
            print(article_count)
        except:
            traceback.print_exc()
    print(nav_count)


def get_news_content(lst, web_url, fpath, fcontent):
    info_dict = {'url': '', 'title': '', 'content': '', 'class': '', 'tag': []}
    fw = open(fcontent, 'a', encoding='utf-8')
    count = 0
    with open(fpath, 'r') as fr:
        for i, line in enumerate(fr):
            # print(i)
            url = re.search(r'http.+\.html', line).group(0)
            print(url)
            count += 1
            print(count)
            try:
                r = get_html_text(url)
                # 将url存入dict
                info_dict['url'] = url
                soup = BeautifulSoup(r, 'html.parser')
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
                section_tip = article.find('section', attrs={'id': 'tip'})
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
                    # art_p = article_content.find_all('p')
                    # print(article_content.contents)
                    # print(article_content)
                    # for ac in article_content.contents:
                    for num, desc in enumerate(article_content.descendants):
                        # match = re.match(r'{pe.begin.pagination}.*{pe.end.pagination}', str(article_content.descendants))
                        # print(match)
                        dc = str(desc)
                        if str(desc.name) == 'a' or str(desc.name) == 'script' or dc == 'wm("arc");':
                            continue
                        # print(desc)
                        # if re.match(r'\s', dc):
                        #     continue
                        if str(desc.name) == 'p' or str(desc.name) == 'br':
                            content += '\n'
                            continue
                        if re.match(r'[{p.*}上一页下一页<b>.*</b>]', dc):
                            continue
                        if dc == '1' or dc == '2' or dc == '3':
                            continue
                        if dc == ' ':
                            continue
                        # if re.match(r'\s*', dc):
                        #     continue
                        content += dc
                        # print(type(desc))

                        # print(type(article_content.descendants))
                        # print(article_content.descendants)
                        # print(article_content)

                    # 文章内容存入dict
                # print(content)
                info_dict['content'] = content
                fw.write(json.dumps(info_dict, ensure_ascii=False) + '\n')
            except:
                traceback.print_exc()
            # if i == 200:
            #     break
        # print(info_dict)
    fr.close()
    fw.close()


'''class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass'''


def main():
    web_url = 'http://www.cnwmz.com'
    lst = []
    fpath = 'F://wmz/wmz.json'
    flist_url = 'F://wmz/500025000_60000120000.txt'
    fname = re.search(r'\d+_\d+', flist_url)
    fcontent = "F://wmz/article_info_" + str(fname.group(0)) + ".txt"
    # 获取文秘站所有导航的页码链接
    # get_nav_addr(lst, web_url)
    # 获取文秘站的所有文章链接
    # get_article_url(lst, web_url, flist_url)
    # 获取想要的内容
    get_news_content(lst, web_url, flist_url, fcontent)
    # sys.stout = Logger("F://wmz/log.txt")


if __name__ == '__main__':
    main()
