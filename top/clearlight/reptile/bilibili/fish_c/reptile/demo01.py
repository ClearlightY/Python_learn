import urllib.request

response = urllib.request.urlopen("http://www.clearlight.top")
html = response.read().decode('utf-8')
print(html)