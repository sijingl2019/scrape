import urllib.request
import urllib.parse
import socket
import urllib.error

response = urllib.request.urlopen('http://www.baidu.com')
# basic code
print(response.read().decode('utf-8'))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

# data param
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# timeout param
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Host': 'httpbin.org'
}

formdata = {
    'name': 'sijingl'
}

data = bytes(urllib.parse.urlencode(formdata), encoding='utf-8')
req = urllib.request.Request(
    url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))

try:
    res = urllib.request.urlopen('https://www.httpbin.org/get', timeout=.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
