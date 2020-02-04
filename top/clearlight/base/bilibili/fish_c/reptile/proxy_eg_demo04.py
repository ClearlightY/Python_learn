import urllib.request

# url = 'http://45.32.164.128/ip.php'
url = 'http://ip.myhostadmin.net/'

proxy_support = urllib.request.ProxyHandler({'http': '177.71.77.202:20183'})

opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
