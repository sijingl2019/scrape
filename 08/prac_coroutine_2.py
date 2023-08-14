import requests
import asyncio
from requests.packages import urllib3
urllib3.disable_warnings()


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url, verify=False)
    return status


tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Tasks:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task Result:', task.result())
