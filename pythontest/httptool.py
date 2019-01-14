# coding=UTF-8
'''页面相关内容信息的处理工具，获取html，发送get post等请求
'''
import io
import gzip

import requests
import os
#from bs4 import BeautifulSoup as bs  # as起到改名作用，以便后面书写
from bs4 import BeautifulSoup as bs
import urllib, urllib3
import YZMimg
import utilty as ut

os.chdir('E:\\Zhou')  # 更改工作目录为桌面
i = 0  # 定义全局变量


# 获取网页
def getHtml(src,session):
    s = session
    try:
        page = s.get(url=src)
        html = page.content
        return html
    except:
        print(' zhou is Failed')


# 获取网页
def postHtml(src,data,session):
    s = session
    try:
        html = s.post(url=src,data=data)
        html=html.content
        return html
    except:
        print('qing is Failed')

#通过登录过去到对应的session，成功的话返回session
def getSessionForLogin(mainUrl,yzmUrl,loginUrl,savePath,username,password):
    #这个是我用的配置的参数
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    mainUrl = mainUrl
    yzmUrl = yzmUrl
    s=requests.session()
    try:
        page=s.get(mainUrl)
        # 下面的操作就相当于刷新了一下验证码
        realPath = YZMimg.getImagAndSave2(yzmUrl, savePath,s)
        code = YZMimg.dealRandomCode(realPath)
        # 然后发送模拟登录
        result=s.post(loginUrl,data=ut.PGPostValues(username, password, code),headers=headers)
        #result = ht.post("http://hnust.hunbys.com/web/login", ut.PGPostValues(username, password, code))
        #html=s.get('http://hnust.hunbys.com/student-learn/739C/640/_F51EAA3/199/__AD/5548/F278C9672171C_AA#0',headers=headers).content
    except:
        print('失败')
        return None
    finally:
        return s



