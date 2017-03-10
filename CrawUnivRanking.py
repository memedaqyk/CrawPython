import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()#判断是否成功获取网页信息
        r.encoding = r.apparent_encoding#替换编码格式
        return r.text
    except:
        return '爬取失败'

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')#同tr.find('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printUnivList(ulist, num):
    tplt = '{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}'#format格式,^代表居中，后面的数字代表宽度，前面的数字代表第几个参数
    print(tplt.format('排名', '学校名称','省份', '总分', chr(12288)))# chr(12288)代表中文字符的空格
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288))) #注意括号个数

def main():
    unifo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(unifo, html)
    printUnivList(unifo, 20)

main()
