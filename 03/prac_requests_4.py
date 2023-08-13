import requests

files = {'file': open('favicon.ico', 'rb')}

# 上传文件
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

# 获取cookie
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)

# headers = {
#     'Cookie': '_zap=b4b102c5-4153-494f-81b3-484cb1782d81; d_c0="APCf7SWSiRSPTiVuyu5VyrqVY1Iviz6pJ5s=|1645609609"; q_c1=14c1fdb0276e4b7baa78c6c74b1c8dd7|1657847538000|1657847538000; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=x5%2FVYlun%2B3BEABBRRQfRCyRRKjwN7d4l; _xsrf=K9LvH2YWkpTYy3dherEN0Y6roGf2Y4q3; __snaker__id=e7fkKGs4Ixc93xi6; YD00517437729195%3AWM_NI=w1itqiWFobUDgrcLWEBb5oskk%2Fe51XDif0TtRRwzJsyRZSonW5zPOK6Jy%2FrpPDjpMar7OurR4Cg3ESlGhm9VNXkj8ZnkPY9VLCbbTgPsHneETR6ZZR4P8xalXVyle7kFeUg%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed9ed67ac9cf796c864b09e8eb6d55a868a8bb0d86f8289a4aff0418bbdf7d2cf2af0fea7c3b92ab5efa795f463959aa183d850a5aeadadd64f82befb90f261a9f1abd6b45488b7aad1d780928eb99bc979bb8e96b4ee6695ebb6b1ce41f696b7d0f17c949ca691d06bb2e98196f15af89da9d4c859b099a88ebc5e8e88a58bbb52aeb5a0babc5e909dae83d76d94ad888fe84f988efabbd95af890f899e4689c8ab78de83da99aabb6e637e2a3; z_c0=2|1:0|10:1690183092|4:z_c0|80:MS4xdUJoUkFnQUFBQUFtQUFBQVlBSlZUZUNvcEdYYkZ1S2dET3JDcU1yb0VTU2ZpLWhaV2FUTE1nPT0=|f2aff6f65c07959a9a3734478da9d467e296ef4b4b84e18403fa830399afcc6c; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1691375611,1691456150,1691466146,1691542828; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1691542828; KLBRSID=4efa8d1879cb42f8c5b48fe9f8d37c16|1691542829|1691542824; SESSIONID=MMOtYGyCYhajr8jts2qpUCzedD7Irx8QlVorK1ParLD; JOID=V18RBUx-IQ30slhkR38x02dER9BSMW9AgekdHgYlS2-cwWIMMFDF3JOyWWVEeY_oCKhVae-TuK9htBy-j1Ov1-s=; osd=UlwVB057Ign2sF1nQ30z1mRARdJXMmtCg-weGgQnTmyYw2AJM1TH3paxXWdGfIzsCqpQauuRuqpisB68ilCr1ek=',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
# }
# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)

# 效果同上
cookies = '_zap=b4b102c5-4153-494f-81b3-484cb1782d81; d_c0="APCf7SWSiRSPTiVuyu5VyrqVY1Iviz6pJ5s=|1645609609"; q_c1=14c1fdb0276e4b7baa78c6c74b1c8dd7|1657847538000|1657847538000; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=x5%2FVYlun%2B3BEABBRRQfRCyRRKjwN7d4l; _xsrf=K9LvH2YWkpTYy3dherEN0Y6roGf2Y4q3; __snaker__id=e7fkKGs4Ixc93xi6; YD00517437729195%3AWM_NI=w1itqiWFobUDgrcLWEBb5oskk%2Fe51XDif0TtRRwzJsyRZSonW5zPOK6Jy%2FrpPDjpMar7OurR4Cg3ESlGhm9VNXkj8ZnkPY9VLCbbTgPsHneETR6ZZR4P8xalXVyle7kFeUg%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed9ed67ac9cf796c864b09e8eb6d55a868a8bb0d86f8289a4aff0418bbdf7d2cf2af0fea7c3b92ab5efa795f463959aa183d850a5aeadadd64f82befb90f261a9f1abd6b45488b7aad1d780928eb99bc979bb8e96b4ee6695ebb6b1ce41f696b7d0f17c949ca691d06bb2e98196f15af89da9d4c859b099a88ebc5e8e88a58bbb52aeb5a0babc5e909dae83d76d94ad888fe84f988efabbd95af890f899e4689c8ab78de83da99aabb6e637e2a3; z_c0=2|1:0|10:1690183092|4:z_c0|80:MS4xdUJoUkFnQUFBQUFtQUFBQVlBSlZUZUNvcEdYYkZ1S2dET3JDcU1yb0VTU2ZpLWhaV2FUTE1nPT0=|f2aff6f65c07959a9a3734478da9d467e296ef4b4b84e18403fa830399afcc6c; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1691375611,1691456150,1691466146,1691542828; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1691542828; KLBRSID=4efa8d1879cb42f8c5b48fe9f8d37c16|1691542829|1691542824; SESSIONID=MMOtYGyCYhajr8jts2qpUCzedD7Irx8QlVorK1ParLD; JOID=V18RBUx-IQ30slhkR38x02dER9BSMW9AgekdHgYlS2-cwWIMMFDF3JOyWWVEeY_oCKhVae-TuK9htBy-j1Ov1-s=; osd=UlwVB057Ign2sF1nQ30z1mRARdJXMmtCg-weGgQnTmyYw2AJM1TH3paxXWdGfIzsCqpQauuRuqpisB68ilCr1ek='
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
print(r.text)
