#!/usr/bin/python
#encoding:utf-8
import re
import  requests
import  time
res=requests.get('http://search.dangdang.com/?key=python&act=input')
prices=re.findall('<span class="search_now_price">&yen;(.*?)</span>',res.text)
for price in prices:
    print(price)
#if __name__=='__main__':
 #   urls=['http://search.dangdang.com/?key=python&act=input&page_index={}'.format(number) for number in range(1,52)]
#for single_url in urls:
   # res(single_url)
   # time.sleep(2)