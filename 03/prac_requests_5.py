import requests

# 保持会话
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# response = requests.get('https://www.12306.cn')
# print(response.status_code)

# 代理服务器（需更换成有效地代理服务器）
proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}
# 带认证信息的代理
proxies = {'https': 'http://user:password@10.10.1.10:3128/',}

requests.get('https://www.taobao.com', proxies=proxies)