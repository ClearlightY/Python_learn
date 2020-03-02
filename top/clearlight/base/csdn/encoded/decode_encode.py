# -*-coding:utf-8
import sys

'''
首先要搞清楚，字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，
即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
总得意思:想要将其他的编码转换成utf-8必须先将其解码成unicode然后重新编码成utf-8,它是以unicode为转换媒介的
如：s='中文'
如果是在utf8的文件中，该字符串就是utf8编码，如果是在gb2312的文件中，则其编码为gb2312。这种情况下，要进行编码转换，都需要先用
decode方法将其转换成unicode编码，再使用encode方法将其转换成其他编码。通常，在没有指定特定的编码方式时，都是使用的系统默认编码创建的代码文件。
如下：
s.decode('utf-8').encode('utf-8')
decode():是解码
encode()是编码
isinstance(s,unicode):判断s是否是unicode编码，如果是就返回true,否则返回false

'''
'''
s='中文'
s=s.decode('utf-8')   #将utf-8编码的解码成unicode
print isinstance(s,unicode)   #此时输出的就是True
s=s.encode('utf-8')           #又将unicode码编码成utf-8
print isinstance(s,unicode)   #此时输出的就是False
'''
print(sys.getdefaultencoding())

s = '中文'
str = s.encode('utf-8')

st = str.decode('utf-8')
print(st)

try:
    st = str.decode('gb2312')
    print(st)
except:
    print("UnicodeDecodeError: 'gb2312' codec can't decode byte 0xad in position 2: illegal multibyte sequence")

print(sys.getdefaultencoding())  # 获取系统默认的编码
# reload(sys)
# sys.setdefaultencoding('utf8')  # 修改系统的默认编码
print(sys.getdefaultencoding())
