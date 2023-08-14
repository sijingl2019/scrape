import requests
from requests.packages import urllib3
urllib3.disable_warnings()
# 保持会话
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# response = requests.get('https://ssr2.scrape.center/', verify=False)
# print(response.status_code)

try:
    r = requests.get('https://www.httpbin.org/get', timeout=1)
except:
    print('timeout')
else:
    print(r.status_code)

# 代理服务器（需更换成有效地代理服务器）
proxies = {
    'http': 'http://140.210.196.193:8060',
    'https': 'https://140.210.196.193:8060'
}
# # 带认证信息的代理
# proxies = {'https': 'http://user:password@10.10.1.10:3128/',}

requests.get('http://www.baidu.com', proxies=proxies, verify=False)
