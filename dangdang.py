#!/usr/bin/python
#encoding:utf-8
import re
import  requests
#import  time
#headers={'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
#def res_link(url):
res=requests.get('http://search.dangdang.com/?key=python&act=input')
prices=re.findall('<span class="search_now_price">&yen;(.*?)</span>',res.text)
for price in prices:
        print(price)
#if __name__=='__main__':
#    urls=['http://search.dangdang.com/?key=python&act=input&page_index={}'.format(number) for number in range(1,52)]
#for url in urls:
#    res_link(urls)
#    time.sleep(2)