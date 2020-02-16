import requests

'''r = requests.get(
    'https://www.amazon.cn/dp/B083ZDFFBF/ref=s9_acsd_hps_bw_c2_x_0_i?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-2&pf_rd_r=CXA8TNPZGFFV8EZR28NM&pf_rd_t=101&pf_rd_p=5a80bc03-4726-4991-ae28-f18724016e76&pf_rd_i=116169071')
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
r.encoding = r.apparent_encoding
print(r.text)
print(r.request.headers)'''

url = 'https://www.amazon.cn/dp/B083ZDFFBF/ref=s9_acsd_hps_bw_c2_x_0_i?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-2&pf_rd_r=CXA8TNPZGFFV8EZR28NM&pf_rd_t=101&pf_rd_p=5a80bc03-4726-4991-ae28-f18724016e76&pf_rd_i=116169071'
try:
    kv = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")

# print(r.status_code)
# print(r.request.headers)
# print(r.text)
