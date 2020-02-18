import requests
import re


def getHTMLText(url):
    try:
        headers = {
            'authority': 's.taobao.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'sec-fetch-user': '?1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'referer': 'https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
            'cookie': 'thw=cn; cna=D5R6FUA1GBgCAd3AtF8ecvUn; hng=CN%7Czh-CN%7CCNY%7C156; miid=1358138455916066906; t=f5496eb15d96bb7326c37202736d0050; v=0; cookie2=1e52f0aff74634d2774388b490a42b8a; _tb_token_=e5a636afe815a; _samesite_flag_=true; sgcookie=Q4tTpNyw0nlSJnWVfQqD; uc3=vt3=F8dBxdz1Sk8EJ7QmhXE%3D&nk2=VAYgjjzLU7%2FmBec%3D&lg2=UtASsssmOIJ0bQ%3D%3D&id2=UNDUK%2FS9o5jAsQ%3D%3D; csg=c9720a35; lgc=7784521%5Cu660E%5Cu5149; dnk=7784521%5Cu660E%5Cu5149; skt=dcbc584dd95816b0; existShop=MTU4MjAwNTMyNQ%3D%3D; uc4=id4=0%40UgckEyzSSPhZof6UkmXUiTUaGiMT&nk4=0%40Vh%2ByyHFmoW%2FwxytP9wpVH9PmibeVzQ%3D%3D; tracknick=7784521%5Cu660E%5Cu5149; _cc_=VFC%2FuZ9ajQ%3D%3D; tg=0; enc=0csVIXUlsoAias1Fqha8M43j8SsybzWteELYl1RvTrY9EjgtBtTEn0DzI0nmLELmgXtQE1OLpVn%2FTfWe5jFcJA%3D%3D; mt=ci=65_1; JSESSIONID=A2751B3E108401F9D44EF79839341F79; l=dBxCAFvgvQGlejptBOCgqsUm5sQ9AIRA_urbn1uBi_5QF6Y6Ah_Oo5AzbFv6cfWfGtYB4Tn8Nrv9-etoil4pJA--g3fPVxDc.; isg=BLS04fOLVqxHRsDVr1QCF3iUhXImjdh38wFe204VYz_CuVQDdp2pBui7PflhRhDP; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTUOLPHrazV%2FQ%3D%3D&tag=8&lng=zh_CN',
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'"view_price":"[\d.]*"', html)
        tlt = re.findall(r'"raw_title":".*?"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = 'Thinkpad笔记本'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods + '&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200218&ie=utf8'
    infoList = []
    print(start_url)
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


if __name__ == '__main__':
    main()
