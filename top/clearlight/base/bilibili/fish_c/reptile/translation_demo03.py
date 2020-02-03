import urllib.request
import urllib.parse
import json
import time

while True:
    content = input('请输入要翻译的内容(输入"q!"退出程序):')
    if content == 'q!':
        break

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    '''
    # 设置访问头, 将访问设为浏览器访问, 而不是代码访问
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    '''

    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    # data['salt'] = '15807113528609'
    # data['sign'] = 'e92895230b64a352dc9d96e8fe500cc7'
    # data['ts'] = '1580711352860'
    # data['bv'] = '901200199a98c590144a961dac532964'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')

    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')

    # print(html)

    target = json.loads(html)
    print('翻译结果: %s' % (target['translateResult'][0][0]['tgt']))
    time.sleep(3)

# print(response.headers)
