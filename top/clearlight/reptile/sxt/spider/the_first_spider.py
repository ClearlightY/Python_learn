from urllib.request import urlopen

url = 'http://www.baidu.com'
# 发送请求
response = urlopen(url)
# 读取内容
info = response.read().decode()
# 打印内容
print(info)
print(response.geturl())
print(response.info())