from bs4 import BeautifulSoup

import requests as r
baseUrl = "http://gz.zu.fang.com"


class Analycis:
    areaList = []  #声明一个空的全局变量
    def get_area_from_net(self):
        response = r.get(baseUrl)
        soup = BeautifulSoup(response.text,'html.parser')
        print(soup)
        dl = soup.findAll("dl", attrs={"id": "rentid_D04_01"})   #获取各地区的url地址(在dl标签中)
        mys = dl[0].find_all("a")     #这里的dl[0]为了防止还有重复的dl
        print (mys)
        for my_a in mys:
            if my_a.text == "不限" or "广州周边" in my_a.text:
                # 这里在github上是用的text,百度了一下说的是调用了get_text()，而之所以没报错python的类部里有text属性，且不是私有的
                continue
            self.areaList.append(my_a.text)

    def getAreaList(self):
        return self.areaList

    def getTotalAvgPrice(self):
        totalAvgPriceList = []
        totalAvgPriceDirList = []
        for index,region in enumerate(self.getAreaList()):
            avgPrice = self.getAreaList()

















