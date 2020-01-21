import requests

# request: 访问网络资源

r = requests.get('http://www.clearlight.top/')
print(r.status_code)
print(r.text)
print(r.encoding)

# 对于带参数的URL, 传入一个dict作为params参数
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)

print(r.content)


# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)

