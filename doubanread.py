import re
import requests

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
info_lists = []
page=[0,20,40]
def get_info(url):
    res = requests.get(url, headers)
    ids = re.findall('<a href="https://www.douban.com/people/\d+/" property="v:reviewer" class="name">(.*?)</a>',res.text,re.S)
    contents=re.findall('<div class="short-content"><p class="spoiler-tip">（.*？）</p>（.*？）&nbsp;(<a href="javascript:;" id="toggle-（\d+）-copy" class="unfold" title="展开">展开</a>)</div>',res.text,re.S)
    replys=re.findall('<a href="https://book.douban.com/review/\d+/#comments" class="reply">(.*?)</a>',res.text,re.S)
    for id,content,reply in zip(ids,contents,replys):
        info = {
            'id':id,
            'content':content,
            'reply':reply
        }
        info_lists.append(info)
if __name__ == '__main__':
    urls=['https://book.douban.com/review/best/?start={}'.format (str(i)) for i in page]
    for url in urls:
        get_info(url)
    #f = open('D:/py/douban.txt', 'a+')
    #try:
     #    f.write(info_lists['id']+'\n')
     #    f.write(info_lists['content'] + '\n')
     #    f.write(info_lists['reply'] + '\n')
     #    f.close()
    #except UnicodeEncodeError:
    #    pass
    print(info_lists)