import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
res=requests.get('https://www.baidu.com/',headers=headers)
soup=BeautifulSoup(res.text,'html.parser')
mp=soup.select('#lg > map > area')
qrcode=soup.select('#qrcode > div > div.qrcode-img')
news=soup.select('#u1 > a:nth-of-type(1)')
dict={'mp':mp,
      'qrcode':qrcode,
      'news':news
      }
print(dict)