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
        traceback.print_exc()



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


def get_news_content(lst, web_url, fpath):
    pass


def main():
    web_url = 'http://www.cnwmz.com'
    lst = []
    fpath = 'F://wmz/wmz.json'
    flist_url = 'F://wmz/article_url1.txt'
    get_nav_addr(lst, web_url)
    get_article_url(lst, web_url, flist_url)
    get_news_content(lst, web_url, fpath)


if __name__ == '__main__':
    main()
