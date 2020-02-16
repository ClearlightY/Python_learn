import requests

kv = {'wd':'Python'}
hd = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
r = requests.get('http://www.baidu.com/s', params=kv, headers=hd)
print(r.status_code)
print(r.request.url)
print(len(r.text))