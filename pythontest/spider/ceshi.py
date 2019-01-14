
# coding=UTF-8
import re
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from requests.exceptions import RequestException
import requests as r
import json
# 获取索引页街拍的方法
def get_page_index(offset,keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response =r.get(url)
        if response.status_code == 200:
            return  response.text
        return None
    except RequestException:
        print('请求索引页错误')
        return None
# 解析索引页的方法
def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')
# 获取详情页的方法
...
# def get_page_detail(url):
#     try:
#         response =r.get(url)
#         if response.status_code == 200:
#             return  response.text
#         return None
#     except RequestException:
#         print('请求详情页错误',url)
#         return None
# # 解析详情页的方法
# def parse_page_detail(html):
#     soup = BeautifulSoup(html,'lxml')   # 使用lxml解析方式来解析title
#     title = soup.select('title')[0].get_text
#     image_pattern = re.compile(' gallery:(.*?);',re.S)
#     result = re.search(image_pattern,html)
#     if result:
#         print(result.group(1))

def main():
    html = get_page_index(0,'街拍')
    print(html)
    zhou = parse_page_index(html)
    for url in parse_page_index(html):
        print(url)
        # html = get_page_detail(url)
        # if html:
        #     parse_page_index(html)

if __name__ == '__main__':
    main()


