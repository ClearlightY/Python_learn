import requests


# url = 'http://wsjkw.hebei.gov.cn/list/zt_gzfy.html'
# # url = 'http://wjw.beijing.gov.cn/wjwh/ztzl/xxgzbd/gzbdzcfg/index.html'
# r = requests.get(url)
# print(r.status_code)
# # r.encoding = 'utf-8'
# print(r.encoding)
# print(r.apparent_encoding)
# # print(r.text)

def getHTMLTest(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200, 引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
       return "产生异常"

# 只有在这个文件下运行才执行, 当在其他文件导入时是不执行的
if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(getHTMLTest(url))