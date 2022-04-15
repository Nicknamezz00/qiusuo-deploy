import requests
import json

url = "http://api.weixin.qq.com/_/cos/getauth"
print(requests.post(url).status_code)