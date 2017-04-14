# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 23:27:17 2015

@author: Administrator
"""

import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#values = {"username":"1016903103@qq.com","password":"XXXX"}
#data = urllib.urlencode(values)

#def getImg(html):
#    reg = r'src="(.+?\.jpg)" pic_ext'
#    imgre = re.compile(reg)
#    imglist = re.findall(imgre,html)
#    x = 0
#    for imgurl in imglist:
#        urllib.urlretrieve(imgurl,r'G:\GitHub\007PythonProject\WebCrawler\Img\%s.jpg' % x)
#        x+=1

def DoItHaveWord(html):
    reg = r'[\u4e00-\u9fa5]+'#r'\u51b7'
    words = re.compile(reg)
    target = re.findall(words,html)
    print len(target)
    if target:
        return True
    else:
        return False
    
def findfirsttiezi():
    for i in range(99):
        html = getHtml("http://tieba.baidu.com/p/"+str(1823966098+i))
#        print html
        if(DoItHaveWord(html)==True):
            print 'success!'
#            break

#print getImg(html)

findfirsttiezi()