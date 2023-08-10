import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/creator/hot-question/hot/0/hour", headers=headers)
print(r.text)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

r = requests.get("https://pan.baidu.com/box-static/disk-theme/theme/white/img/logo@2x.png")
with open('favicon.ico', 'wb') as f:
    f.write(r.content)

