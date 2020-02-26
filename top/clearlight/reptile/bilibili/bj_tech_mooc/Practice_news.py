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


def get_topic_addr(lst, news_web_url):
    index = ['', '_1', '_2', '_3']
    count = 0
    for i in index:
        url = news_web_url + 'index' + str(i) + '.html'
        print(url)
        r = get_html_text(url)
        soup = BeautifulSoup(r, "html.parser")
        a = soup.find_all('a')

        for i in a:
            try:
                href = i.attrs['href']
                new_addr = re.search(r'\d{6}/t\d{8}_\d{7}.html$', href)
                if new_addr:
                    count += 1
                    lst.append(new_addr.group(0))
            except:
                traceback.print_exc()
    print(lst)
    print(count)
    return count
    # print(lst[0])


def get_news_content(lst, news_web_url, fpath):
    fw = open(fpath, 'a', encoding='utf-8')
    for item in lst:
        news_text = get_html_text(news_web_url + str(item))
        try:
            if news_text == '':
                continue
            article_info = {'title': '', 'content': '', 'issue': '', 'time': '', 'source': ''}
            soup = BeautifulSoup(news_text, "html.parser")
            # article = soup.find('div', attrs={'class': 'article0'})
            article_info['title'] = soup.find('div', attrs={'class': 'articleTitle'}).string
            time_source = soup.find('div', attrs={'class': 'articleSubTitle'}).string
            # time = time_source.find(string=re.compile(r'\d{4}-\d{2}-\d{2}'))
            time = re.search(r'(\d{4})[年-](\d{1,2})[月-](\d{1,2})', time_source)
            if time:
                article_info['time'] = time.group(0)
            source = re.search(r'[\u4e00-\u9fa5]{2,}[网府厅部报委会局]', time_source)
            # source = re.search(r'来源[:：] ?(.+[网府厅部报委会局])', time_source)
            if source:
                article_info['source'] = source.group(0)
            else:
                article_info['source'] = '北京市卫生健康委'

            # 返回bodyTxt下的所有内容
            article_text = soup.find('div', attrs={'class': 'bodyTxt'})

            # 获取文章内容
            article_content = soup.find('div', attrs={'class': 'article'})
            content = article_content.find_all('p')
            # print(content)

            content_list = []
            for num, desc in enumerate(article_content.descendants):
                dc = str(desc)
                tag = re.search(r'(<.+>.*</.+>|<.+/>|<.+>|</.+>)', dc)
                if tag:
                    # print('-----------------')
                    # print(tag.group(0))
                    # content_list.append('\n')
                    continue
                # if str(desc.name) == 'p' or str(desc.name) == 'strong' or str(desc.name) == ' str(desc.name) == 'br' or str(desc.name) == 'div' or str(desc.name) == 'img' or str(desc.name) == 'a' or str(desc.name) == 'center' or str(desc.name) == 'span':
                #
                #     continue
                if dc == ' ' or dc == '点击下载：':
                    continue
                file = re.search(r'.+\.(doc|ppt|excl|zip)', dc)
                if file:
                    # print('****************')
                    # print(file.group(0))
                    if dc == file.group(0):
                        continue
                content_list.append(dc + '\n')
                print(dc)
                if num == 3:
                    break

            article_info['content'] = content_list
            # 将每条信息写到文件中
            fw.write(json.dumps(article_info, ensure_ascii=False) + '\n')
            # print(article_info)
        except:
            traceback.print_exc()


def main():
    new_web_url = 'http://wjw.beijing.gov.cn/wjwh/ztzl/xxgzbd/gzbdzcfg/'
    lst = []
    fpath = 'F://practice/policy/beijing.txt'
    get_topic_addr(lst, new_web_url)
    get_news_content(lst, new_web_url, fpath)


if __name__ == '__main__':
    main()
