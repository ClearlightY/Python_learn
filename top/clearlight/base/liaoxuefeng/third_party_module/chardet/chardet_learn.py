import chardet
# 检测编码

# 检测bytes 编码
print(chardet.detect(b'Hello, world!'))

data = ('你好我是'.encode('UTF8'))
print(chardet.detect(data))

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))

data = b'\xc0\xeb\xc0\xeb\xd4\xad\xc9\xcf\xb2\xdd\xa3\xac\xd2\xbb\xcb\xea\xd2\xbb\xbf\xdd\xc8\xd9'
print(chardet.detect(data))