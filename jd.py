import re
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
info_lists=[]
def get_info(url):
    res=requests.get(url)
    tittles=re.findall('<em><font class="skcolor_ljg">python</font>(.*?)</em>',res.text,re.S)
    prices=re.findall('<strong class=\w data-done="1"><em>￥</em><i>(.*?)</i></strong>',res.text,re.S)
    shops=re.findall('<a class="curr-shop" target="_blank" onclick="searchlog(1,\d,0,58)" href="//mall.jd.com/index-\d.html" title="(.*?)">(.*?)</a>',res.text,re.S)
    for tittle,price,shop in zip(tittles,prices,shops):
        info = {
            'tittle':tittle,
            'price':price,
            'shop':shop
        }
        info_lists.append(info)
if __name__ == '__main__':
    urls = ['https://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=python&page={}&s=59&click=0'.format(str(i)) for i in range(1,19)]
    for url in urls:
        get_info(url)
        time.sleep(2)
    for info_list in info_lists:
        print(info_list)