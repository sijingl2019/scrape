import requests

# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)
# print(r.headers)

# r = requests.get('http://httpbin.org/get')
# print(r.text)

# data = {
#     'name': 'germey',
#     'age': 22
# }
# r = requests.get("http://httpbin.org/get", params=data)
# print(r.text)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

import re
r = requests.get('https://ssr1.scrape.center/')
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
