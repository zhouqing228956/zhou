# coding=UTF-8
'''处理验证码部分，包含了获取验证的图片保存本地，本地获取识别获取信息，模拟返回数值
'''
import pytesseract
from PIL import Image
import urllib, urllib3
import time
import socket


#获取验证码图片，然后保存到本地，返回地址,需要把session传进来
def getImagAndSave2(url,path,sess):
    img_url = url #'http://hnust.hunbys.com/verifycode/getverifycode.action?t=1542341506341
    name=(int)(time.time())
    realpath=path +str(name)+'.jpg'
    socket.setdefaulttimeout(30)
    try:
        image = sess.get(img_url, headers=sess.headers).content
        # 保存到本地
        with open(realpath, "wb") as f:
            f.write(image)
            f.close()
    except:
        print ('save failed')
    finally:
        return realpath

#获取到地址下的img，返回图片中的验证数字
def dealRandomCode(path):
    blnnum=False
    image_info=None
    try:
        info = Image.open(path)
        image_info = pytesseract.image_to_string(info, lang='eng')
        print(image_info)
        blnnum = str(image_info).isdigit()
    except:
        print (path,' read error')
    finally:
        if blnnum:
            return image_info
        else:
            return str('1111')
