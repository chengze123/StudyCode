# -*- coding: utf-8 -*-
# encoding='utf-8'
import re
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from urllib import request
import datetime

# 用request和BeautifulSoup处理网页
def requestOver(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# 从网页下载标题和内容到txt文档
def download(title, url, y):
    soup = requestOver(url)
    tag = soup.find('div', class_="left_zw")
    if(tag == None):
        return 0
    # print(type(tag))
    # print(tag.get_text())
    title = title.replace(':', '')
    title = title.replace('"', '')
    title = title.replace('|', '')
    title = title.replace('/', '')
    title = title.replace('\\', '')
    title = title.replace('*', '')
    title = title.replace('<', '')
    title = title.replace('>', '')
    title = title.replace('?', '')
    # print(tag.get_text())
    content = ""
    for p in tag.findAll('p'):
        if (p.string != None):
            content = content + p.string
    #保存的文件要存在
    filename = r'D:\代码学习' + title + '.txt'
    with open(filename, 'w', encoding='utf-8', errors='ignore') as file_object:
        file_object.write('           ')
        file_object.write(title)
        file_object.write(tag.get_text())
    print('正在爬取第', y, '个新闻', title)

# 爬虫具体执行过程
def crawlAll(url, y):
    soup = requestOver(url)
    for s in soup.findAll("div", class_="content_list"):
        for tag in s.findAll("li"):
            sp = tag.findAll("a")
            if("财经" in str(sp)):
                title = list(sp)[1].string
                urlAll = "http://www.chinanews.com" + str(list(sp)[1])[9:str(list(sp)[1]).find("shtml")+5]
                try:
                    download(title, urlAll, y)
                except Exception:
                    print("第" + str(y) + "个新闻爬取失败")
                else:
                    y += 1
    return y

if __name__ == '__main__':
    y = 1
    url1 = "http://www.chinanews.com/scroll-news/"
    date = "2021/0315"
    url2 = "/news.shtml"
    for i in range(3650):
        date1 = datetime.datetime.strptime(date, "%Y/%m%d")
        date2 = datetime.timedelta(days=-1)
        date = (date1 + date2).strftime("%Y/%m%d")
        target_url = url1 + date + url2
        print(target_url)
        y = crawlAll(target_url, y)
