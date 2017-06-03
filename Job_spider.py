#-*- coding: utf-8 -*-
'''
downhtml 爬取一级页面，爬取结果先交由 attribute 处理，生成 attribute.txt 文件，然后再爬取职位详细页面链接，
之后将链接交由 downhtml 爬取二级页面，爬取的结果交由 description 程序处理，生成 description.txt 文件
'''
import requests
from lxml import etree
import time
import random
import re

def downhtml(url):
    '''爬取页面'''
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent, "Accept-Language": "zh-cn", 'Connection':'keep-alive','Accept-Encoding': 'gzip,deflate'}
    html = requests.get(url, headers = headers).content
    #return etree.HTML(html)
    return html

def Job_url(html):
    '''职位链接'''
    html = etree.HTML(html)
    job_url = html.xpath("//td[@class = 'zwmc']/div/a/@href")
    return job_url

def attribute(html):
    '''职位属性'''
    job_money = re.findall(r'<td class="zwyx">(.*)</td>', html)
    job_city  = re.findall(r'<td class="gzdd">(.*?)</td>', html)
    html = etree.HTML(html)
    job_attr = html.xpath("//div[@class='clearfix']/ul/li[1]/span/text()")

    f = open("attribute.txt", "a")
    for i in job_attr:
        f.write(i.encode('utf8') + '\n')
    f.close()
    f = open("city_money.txt", 'a')
    for i in range(len(job_city)):
        f.write(job_city[i] + '\t')
        f.write(job_money[i] + '\n')
    f.close()

def description(job_url):
    '''职位描述'''
    f = open('description.txt', 'a')
    for i in job_url:
        sec = int(random.random()*7)
        print 'Please wait', sec, 'sec'
        time.sleep(sec)
        try:
            html = downhtml(i)
            html = etree.HTML(html)
            job_desc = html.xpath("//div[@class='tab-inner-cont']/p/text()")
            for j in job_desc:
                 j = re.sub('\s','',j)
                 f.write(j.encode('utf8') + '\n')
            print u'网址：', i, u'已记录'
        except:
            print i, u'记录失败'
    f.close()

if __name__ == '__main__':
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&kw=python&isadv=0&sg=2c728cdd200d47d185d1b1f6882ed441&p='
    for i in range(90):
        l = str(i)
        html = downhtml(url+l)
        attribute(html)
        job_url = Job_url(html)
        description(job_url)
        print '总进度:', (i+1)/90.0*100, '%'
