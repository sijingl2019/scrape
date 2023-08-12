from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://140.210.196.193:8060',
    'https': 'https://140.210.196.193:8060'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
