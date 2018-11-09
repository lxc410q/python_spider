import requests
from lxml import etree
def get_info(url):
    html=requests.get(url)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//*[@id="head"]/div')

    for info in infos:
        news=info.xpath('//*[@id="u1"]/a[1]/text')[0]
        hao=info.xpath('//*[@id="u1"]/a[2]/text')[0]
        map=info.xpath('//*[@id="u1"]/a[3]/text')[0]
        zhuye=info.xpath('//*[@id="setf"]/text')[0]

