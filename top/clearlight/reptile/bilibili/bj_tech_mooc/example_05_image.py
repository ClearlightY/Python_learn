import requests
import os

'''
获取网页中的图片, 并将该二进制文件保存到本地
'''
'''path = "F:/abc.png"
url = "http://www.clearlight.top/images/bottom.png"
r = requests.get(url)
print(r.status_code)
with open(path, 'wb') as f:
    f.write(r.content)
# print(r.content)
r.close()'''

# 图片爬取全代码
# url = 'http://www.clearlight.top/images/bottom.png'
# url = 'http://www.clearlight.top/video/%E8%87%B4%E6%9C%80%E7%BE%8E%E7%9A%84%E4%BD%A0.mp4'
url = 'http://www.clearlight.top/homepage/music/love.mp3'
root = 'F://pics//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
