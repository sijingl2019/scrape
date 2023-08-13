from requests import Request, Session
url = 'https://www.httpbin.org/post'
data = {'name': 'germy'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
}

s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(request=req)
r = s.send(prepped)
print(r.text)
