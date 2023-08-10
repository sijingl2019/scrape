from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin
from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import unquote 

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))

params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

# 转换成字典
query = 'name=germey&amp;age=22'
print(parse_qs(query))

# 转换成元组
query = 'name=germey&amp;age=22'
print(parse_qsl(query))

# 转成url编码
keyword = ' 壁纸 '
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
