import requests
import re
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
soup = BeautifulSoup(r.text, "html.parser")

# 查找所有a标签
print(soup.find_all('a'))
print(type(soup.find_all('a')))
# <class 'bs4.element.ResultSet'>

for tag in soup.find_all('a'):
    print(tag.string)
# 显示a 和 b 标签
print(soup.find_all(['a', 'b']))

# 显示soup的所有标签信息
for tag in soup.find_all(True):
    print(tag.name)

# 使用正则表达式来查找含有b的标签
for tag in soup.find_all(re.compile('b')):
    print(tag.name)

# 查找p标签含有course的内容
print(soup.find_all('p', 'course'))

# 查找id属性为link1的内容
print(soup.find_all(id='link1'))

# 查找id属性为link的内容 没有则返回[]
print(soup.find_all(id='link'))

# 使用re模块来查找id属性包含link的内容
print(soup.find_all(id=re.compile('link')))

# 设置recursive参数为False, 这时从soup的子节点进行检索, 而不会去检索子孙节点的内容
print(soup.find_all('a', recursive=False))

# 检索字符串是否存在
print(soup.find_all(string="Basic Python"))

# 检索字符串是否含有python, 通过re
print(soup.find_all(string=re.compile('Python')))
print(soup(string=re.compile('Python')))