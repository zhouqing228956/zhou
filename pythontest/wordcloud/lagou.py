from urllib.parse import urlencode

import requests as  r
import re
import json

#
# url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
# #
# # data = {'first':'false',
# #         'pn': 3,
# #         'kd': 'java'
# #         }
# # header = {
# #           'Origin': 'https://www.lagou.com',
# #           'Referer': 'https://www.lagou.com/jobs/list_java?city=%E5%85%A8%E5%9B%BD',
# #           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
# #           }
# # #遍历网页循环
# # for n in range(1,2):   #[1,2),左闭右开
# #     data = {'first': 'false',
# #             'pn': n,
# #             'kd': 'java'
# #             }
# #     html = r.post(url,data=data,headers = header)
# #     #采集数据的招聘信息循环的公司
# #     for m in range(len(html.json()['content']['positionResult']['result'])):
# #         print(html.json()['content']['positionResult']['result'][m]['positionName'])

data = {
  'callback': 'getUCGI8835599773654568',
  'g_tk': '5381',
   'sonpCallback': 'getUCGI8835599773654568',
'loginUin': '0',
'hostUin': '0',
'format': 'jsonp',
'inCharset': 'utf8',
'outCharset': 'utf-8',
'notice': '0',
'platform': 'yqq',
'needNewCode': '0',
'data': '{"singerAlbum":{"method":"get_singer_album","param":{"singermid":"0025NhlN2yWrP4","order":"time","begin":0,"num":30,"exstatus":1},"module":"music.web_singer_info_svr"}}'
}

url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?'
response = r.get(url,params=data)
print(response.text)
searchObj = re.search('getUCGI8835599773654568\((.*)$',response.text, re.M | re.I)
albums = searchObj.group(1)

print(albums)










