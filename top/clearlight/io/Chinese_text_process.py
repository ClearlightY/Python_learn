import codecs as cs
import os

fr = open('test.txt', encoding='utf-8', errors='ignore')
all_utf8 = fr.read()
# all_utf8.decode('utf-8')
print(all_utf8)

'''for p, d, fs in os.walk('test'):
    for f in fs:
        blob = open(os.path.join(p, f)).read()
        m = magic.Magic(mime_encoding=True)
        encoding = m.from_buffer(blob)
        if encoding == 'utf_16be':
            encoding = 'utf_16_be'
        ......
        with cs.open(os.path.join(p, f), 'r', encoding):
            some operations'''