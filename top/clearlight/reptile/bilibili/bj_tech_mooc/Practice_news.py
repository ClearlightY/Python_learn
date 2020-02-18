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
    index = ['', '_1', '_2']
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
            # 查看文本中是否含有发文字号, 若含有, 则以列表的形式将文本进行划分
            issue_txt = article_text.find_all(string=re.compile(r'[ \u3000\t]*(.{1,5}[指发办电]? ?〔\d{4}〕 ?第?\d{1,3}号)'))
            # print(len(issue_txt))

            # 若文本含有文号, 则列表长度不为0
            if len(issue_txt) != 0:
                # 遍历列表
                for i in issue_txt:
                    # 返回符合re符合的字符串
                    issue = re.search(r'[ \u3000\t]*(.{1,5}[指发办电]? ?〔\d{4}〕 ?第?\d{1,3}号)', i)
                    # 若是不为空, 则将返回结果存到字典中
                    if issue:
                        article_info['issue'] = issue.group(0)
                        # 以最近的文号为准, 有漏洞(若是文章中含有文号, 却不是本文的, 则获取错误, 需要修改)
                        break

            # 获取文章内容
            content_list = []
            article_content = soup.find('div', attrs={'class': 'article'})
            content = article_content.find_all('p')
            # print(content)
            for p in content:
                # print(p)
                # print(type(p))
                # print(type(p.string))
                if p.string is not None:
                    content_list.append(str(p.string) + '\n')

            article_info['content'] = content_list
            # 将每条信息写到文件中
            fw.write(json.dumps(article_info, ensure_ascii=False) + '\n')
            # print(article_info)
        except:
            traceback.print_exc()


def main():
    new_web_url = 'http://wjw.beijing.gov.cn/wjwh/ztzl/xxgzbd/gzbdzcfg/'
    lst = []
    fpath = 'F://beijing.txt'
    get_topic_addr(lst, new_web_url)
    get_news_content(lst, new_web_url, fpath)


if __name__ == '__main__':
    main()
