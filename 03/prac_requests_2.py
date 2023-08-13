import requests

r = requests.get(
    "https://pan.baidu.com/box-static/disk-theme/theme/white/img/logo@2x.png")
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
}
r = requests.get('https://ssr1.scrape.center', headers=headers)
print(r.text)
