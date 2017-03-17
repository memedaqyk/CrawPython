import requests
import re

# 获取页面的HTML函数
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()# 检查是否获取页面成功
        r.encoding = r.apparent_encoding # 修改页面的编码格式
        return r.text
    except:
        return "爬取失败"

def parsePage(ilt, html): # ilt是一个列表，存储商品和价格
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html) # 获取商品价格，\表示转义
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html) # ？表示最小区间
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1]) # 用split函数提取
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print('提取失败')
        
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}" # 槽函数
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(count, g[0], g[1])

def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()
