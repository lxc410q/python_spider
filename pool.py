from multiprocessing import pool
import requests
from lxml import etree
import pymongo
from multiprocessing import pool

client=pymongo.mongo_client('localhost',27017)
mydb=client['mydb']
douban=mydb['douban']

def get_douban(url):
    html=requests.get(url)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//div[@class="indent"]/tr')

for info in infos:
    try:
      top=info.xpath('div/tr/td[2]/a/@title')

    except IndexError
        pass
if__name__=='__main__':
    urls=['https://book.douban.com/top250?start={}'.format(str(i) for i in) range(0,250,25)]
       pool=pool(processes=4)
    pool.map(get_douban,urls)