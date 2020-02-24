import json
import re
import traceback
from threading import Thread
from queue import Queue
from lxml import etree
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
        if r.status_code == 200:
            return r.text
    except:
        # traceback.print_exc()
        return 404


# 获取url文本的类
class CrawlInfo(Thread):
    def __init__(self, url_queue, html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        info_dict = {'url': '', 'title': '', 'content': '', 'class': '', 'tag': []}
        # count = 0
        while self.url_queue.empty() == False:
            with open('F://wmz/article_info_500000_600000_1.json', 'a', encoding='utf-8') as f:
                url = self.url_queue.get()
                print(url)
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
                web_url = re.search(r'http://www.cnwmz.com/html/\d+/\d+', url)
                # print(web_url)
                content = ''

                for j in range(20):
                    # 尝试文章是否有多页, 若有多页的话, 则改变j的值进行内容添加
                    if j != 0:
                        j += 1
                        wu = str(web_url.group(0)) + '_' + str(j) + '.html'
                        # print(wu)
                        wu_text = get_html_text(wu)
                        if wu_text == 404:
                            break
                        soup = BeautifulSoup(wu_text, 'html.parser')
                        # print(soup)
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
                        if dc == '1' or dc == '2' or dc == '3':
                            continue
                        if dc == ' ':
                            continue
                        content += dc

                # 文章内容存入dict
                # print(content)
                info_dict['content'] = content
                f.write(json.dumps(info_dict, ensure_ascii=False) + '\n')
                f.flush()
        print(info_dict)
        f.close()
    # fh.write(json.dumps(count, ensure_ascii=False) + '\n')



def main():
    fhistory_num = 'F://wmz/history_read_num.txt'
    flist_url = 'F://wmz/500000_600000.txt'
    # fname = re.search(r'\d+_\d+_?\d*_?\d*', flist_url)
    # fcontent = "F://wmz/article_info_" + str(fname.group(0)) + ".json"

    # 存储url的容器
    url_queue = Queue()
    # 存储内容的容器
    html_queue = Queue()

    with open(flist_url, 'r') as fr:
        num = input("请输入想要开始的行号:")
        n = int(num) - 1
        count = n
        for line in fr.readlines()[n:]:
            # print(i)
            url = re.search(r'http.+\.html', line).group(0)
            # 向容器中添加url
            url_queue.put(url)
    crawl_list = []
    for i in range(0, 50):
        crawl1 = CrawlInfo(url_queue, html_queue)
        crawl_list.append(crawl1)
        crawl1.start()

    # 等待爬取网页信息的线程完成, 在执行主线程
    for crawl in crawl_list:
        crawl.join()

    fr.close()
    # parse_list = []
    #
    # for i in range(0, 5):
    #     parse = ParseInfo(html_queue)
    #     parse_list.append(parse)
    #     parse.start()
    # for parse in parse_list:
    #     parse.join()
    # 获取想要的内容
    # get_news_content(flist_url, fcontent, fhistory_num)

if __name__ == '__main__':
    main()
