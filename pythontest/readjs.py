# coding=UTF-8
'''读取js
'''

import execjs
import io
def get_js():
    f = io.open('F:\\pythontest\\url.js', 'r',encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr
def get_des_psswd(strid):
    jsstr = get_js()
    ctx = execjs.compile(jsstr) #加载JS文件
    return (ctx.call('getUrl', '7', strid))