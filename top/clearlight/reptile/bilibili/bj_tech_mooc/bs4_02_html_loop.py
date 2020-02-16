import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

# print(soup.prettify())

print(soup.head)
print(soup.head.contents)
print(soup.body)
print(soup.body.contents)
# 获取body儿子节点的数量
print(len(soup.body.contents))
# 检索列表中第二个
print(soup.body.contents[-2])
print(type(soup.body.contents))

# 标签数的下行遍历
for child in soup.body.children:
    print(child)

# for child in soup.body.descendants:
#     print(child)

# 标签数的上行遍历
# 遍历a标签的所有父节点
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# title的父标签
print(soup.title.parent)

# 标签树的平行遍历
# 遍历后续节点
for sibling in soup.a.next_siblings:
    print(sibling)

# 遍历前续节点
for sibling in soup.a.previous_siblings:
    print(sibling)

print(type(soup.p.children))
print(type(soup.p.parents))