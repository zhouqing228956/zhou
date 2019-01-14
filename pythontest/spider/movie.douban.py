# coding=UTF-8

import json
import requests as r
from bs4 import BeautifulSoup

'''
url = https://movie.douban.com/top250
https://movie.douban.com/top250?start=25&filter=
rannge(start,end,list)list表示间隔，如：0，25，50
url=[https://movie.douban.com/top250?start='+ str(n)+'&filter=' for n in range(0,250,25)]
'''
i=0
def rul():
    urls = ['https://movie.douban.com/top250?start='+str(n)+'&filter ='for n in range(0,250,25)]
    for url in urls:
        con_data = r.get(url)
        soup = BeautifulSoup(con_data.text,'html.parser')
        title = soup.select('div .hd > a')
        describe = soup.select('.inq')
        
        rate = soup.select('span.rating_num')
        image = soup.select('img[src]')
        print(type(title))
        for title,describe ,rate,image in zip(title,describe,rate,image):
            data = {
                "电影名" : list(title.stripped_strings)[0],
                "电影描述":describe .get_text(),
                "分数" : rate.get_text(),
                "图片" : image.get('src')
            }
            write(data)
            global i
            i+=1
            fileName = str(i) + '、'+data['电影名']+' '+data['分数']+'分.jpg'
            pic = r.get(data['图片'])
            with open('C:\\Users\\Administrator\\Desktop\\豆瓣250-picture\\'+fileName,'wb') as photo:
                photo.write(pic.content)
            print(data)
def write(con):
    with open('C:\\Users\\Administrator\\Desktop\\豆瓣250.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(con,ensure_ascii=False) + '\n')
        f.close()

def main():   #如有带参函数可以在此处处理

    rul()
if __name__ == '__main__':
    main()







