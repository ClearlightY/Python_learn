import requests
from bs4 import BeautifulSoup

'''r = requests.get("http://python123.io/ws/demo.html")
print(r.text)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())'''

soup2 = BeautifulSoup(open("F://pics/541724.html"), "html.parser")
# print(soup2.prettify())
print(soup2.find_all(attrs={"class": "songLyricCon"}))
