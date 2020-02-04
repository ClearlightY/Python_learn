import urllib
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# 处理异常的第一种写法
req = urllib.request.Request('http://www.clearlight.top/clear')
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    pass

# 处理异常的第一种写法
req = urllib.request.Request('http://www.baiduyyy.com')
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    pass
