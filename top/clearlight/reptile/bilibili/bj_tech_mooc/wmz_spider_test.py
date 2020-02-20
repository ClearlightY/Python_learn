import requests
import re
from bs4 import BeautifulSoup
import traceback
import json


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
    with open(fpath, 'r') as fr:
        for i, line in enumerate(fr):
            # print(i)
            url = re.search(r'http.+\.html', line).group(0)
            print(url)
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
                con = ['']
                for j in range(30):
                    # 尝试文章是否有多页, 若有多页的话, 则改变j的值进行内容添加
                    if j != 0:
                        j += 1
                        wu = str(web_url.group(0)) + '_' + str(j) + '.html'
                        wu_text = get_html_text(wu)
                        if wu_text == 200:
                            break
                        soup = BeautifulSoup(wu_text, 'html.parser')
                    article_content = soup.find('section', attrs={'id': 'article'})
                    art_p = article_content.find_all('p')
                    print(len(art_p))

                    if len(art_p) < 2:
                        for ac in article_content:
                            name = str(ac.name)
                            if name == 'br':
                                content += '\n'
                            if str(ac.string) == 'None' or str(ac.string) == 'wm("arc");':
                                continue
                            # print(ac.string)
                            content += str(ac.string)
                            # print(content)
                        # con[0] = content
                    else:
                        article1 = soup.find('article', attrs={'id': 'con_l'})
                        art = article1.find_all('p')
                        # print(art)
                        for j, a in enumerate(art):
                            # if a.attrs['class'] == 'page_css':
                            #     continue
                            # print(art[j])
                            # print(type(art[j]))
                            # if art[j].find('class', attrs={'class': 'page_css'}):
                            #     print(1)
                            # continue
                            m = art[j].find('a')
                            if art[j].find('a'):
                                if str(art[j].find('a').string) == '上一页':
                                    continue
                            # print(a.contents)
                            for m in a.contents:
                                content += str(m.string)
                                # print(m)
                            # print(content)
                            content += '\n'
                        # con[0] = content
                    # print(content)
                    # 文章内容存入dict
                info_dict['content'] = content
                fw.write(json.dumps(info_dict, ensure_ascii=False) + '\n')
            except:
                traceback.print_exc()
            if i == 0:
                break
        # print(info_dict)
    fr.close()
    fw.close()


def main():
    web_url = 'http://www.cnwmz.com'
    lst = []
    fpath = 'F://wmz/wmz.json'
    flist_url = 'F://wmz/article_url2.txt'
    fcontent = "F://wmz/article_info_test.txt"
    # 获取文秘站所有导航的页码链接
    # get_nav_addr(lst, web_url)
    # 获取文秘站的所有文章链接
    # get_article_url(lst, web_url, flist_url)
    # 获取想要的内容
    get_news_content(lst, web_url, flist_url, fcontent)


if __name__ == '__main__':
    main()
