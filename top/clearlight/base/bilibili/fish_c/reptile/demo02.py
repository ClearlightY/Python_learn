import urllib.request

response = urllib.request.urlopen('http://placekitten.com/g/1080/960')
cat_img = response.read()

with open('cat_1080_960.jpg', 'wb') as f:
     f.write(cat_img)

print(response.geturl())
print(response.info())
print(response.getcode())