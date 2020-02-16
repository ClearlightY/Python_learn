import requests

# 查询ip地址
'''ip = '36.98.57.11'
url = "http://ip138.com/iplookup.asp?ip="+ip+"&action=2"
r = requests.get(url + ip)
print(r.status_code)
print(r.text[-500:])'''

# ip地址查询全代码
ip = '36.98.57.11'
url = "http://ip138.com/iplookup.asp?ip="+ip+"&action=2"
# print(url+ip)
try:
    r = requests.get(url)
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")