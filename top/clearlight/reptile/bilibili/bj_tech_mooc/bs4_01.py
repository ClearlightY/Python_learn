import requests
from bs4 import BeautifulSoup

url = "http://python123.io/ws/demo.html"
# url = "http://www.clearlight.top"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

# Tag
# 获取网页的标题
print(soup.title)
print(type(soup.title))
# 获取html的a标签的内容
# 默认获取第一个标签
print(soup.a)
print(type(soup.a))
'''# 获取所有的a标签
for soup.a in soup:
    print(soup.a)'''

# Name
# 获取标签的名字
print('标签名字:', soup.a.name)
# a标签父亲的名字
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
print(type(soup.a.parent.parent.name))

# Attributes
# 获取属性信息
tag = soup.a
print("属性", tag.attrs)
# 获取class属性的值
print(tag.attrs['class'])
print(tag.attrs['href'])
# 获取标签类型
print(type(tag.attrs))
# 查看tag得类型
print(type(tag))

# NavigableString
# 获取a标签的字符串信息
print(soup.a.string)
print(soup.p.string)
print(type(soup.p.string))

new_soup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
print(new_soup.b.string)
print(type(new_soup.b.string))
print(new_soup.p.string)
print(type(new_soup.p.string))
