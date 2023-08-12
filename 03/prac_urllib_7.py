from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url('http://www.baidu.com/robots.txt')
rp.read()
print(rp.can_fetch('Baiduspider', 'http://www.baidu.com/'))
print(rp.can_fetch('Baiduspider', 'http://www.baidu.com/homepage'))
print(rp.can_fetch('Googlebot', 'http://www.baidu.com/homepage'))
