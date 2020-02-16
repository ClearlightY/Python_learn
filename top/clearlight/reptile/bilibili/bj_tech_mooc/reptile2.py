import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
p = requests.request('GET', 'http://python123.io/ws', params=payload)
print(p.url)
print(p)
