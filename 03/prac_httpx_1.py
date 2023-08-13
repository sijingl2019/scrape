import httpx

# import requests
# url = 'https://spa16.scrape.center'
# res = requests.get(url)
# print(res.text)

# res = httpx.get('https://www.httpbin.org/get')
# print(res.status_code)
# print(res.headers)
# print(res.text)


url = 'https://spa16.scrape.center'
# 必须手动开启http2
client = httpx.Client(http2=True)
res = client.get(url)
print(res.text)
