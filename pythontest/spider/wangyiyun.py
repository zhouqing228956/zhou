
# coding=UTF-8
import urllib
from urllib.parse import urlencode
import requests as r
from requests.exceptions import RequestException
import json


headers = {
    "Refer":"https://music.163.com/song?id=1306400549",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
data = {
    "params": "q/toKNH5MvNv1VNlSIb9zUBnKtQqa5zOrh5rOiyNFVm0tDZjnS0pVKVXiTqj3tKnuw6drHeLPCjvnvpuzoHfvhepcvOVpkt8s8CzFEo72PQWcFGBXXrwqtrA+UVh6WK0lBzKnG5GnKsYQpW3ft/imjzf8rmFxI89pleejQxLN4SesQKddjtp4UOU4oG4/bsn",
    "encSecKey": "ae09e41a42bdb6da5303b2a2a7dede3fd7c5da71811700f48a3ce05023251f12fac530c8a8ed503575e568c954223a73b2208f2ba700c4b3fc807be173c7aa66af057b17d6bb311f8770fe3efb89f6c1818efd7d6e8407dd5f261db5992b9b632825da850a872e0432e34b2e0847e2debfd42e65b1f1a6c6ece94ba1e18583f0"
}
url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_1306400549?csrf_token="
def write(content):
    with open('qing.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+ '\n')
        f.close()

k=(urllib.request.urlopen(urllib.request.Request(url=url,data=urlencode(data).encode('utf-8'),headers=headers)).read().decode('utf-8'))
print(type(k))
for eve_data in json.loads(k)['comments']:
    print(eve_data['content'])
    write(eve_data['content'])



# print(html)
# k=json.loads(html['comments'])
# for comment in json.loads(html['comments']):
#     print(comment)

# print(r.get(url,headers=headers).text)
# def get_data():
#     try:
#         response = r.post(url,headers=headers)
#         if response.status_code == 200:
#             return response.text
#         return None
#     except  RequestException:
#         print("请求错误")
#         return None
# def main():
#    html = get_data()
#    print(html)
# if __name__ == '__main__':
#     main()


