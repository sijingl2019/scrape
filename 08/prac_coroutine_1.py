import requests
import asyncio
from requests.packages import urllib3
urllib3.disable_warnings()


# async def execute(x):
#     print('Number:', x)
#     return x
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')

# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# # 效果同上
# # task = asyncio.ensure_future(coroutine)
# print('Task: ', task)
# loop.run_until_complete(task)
# print('Task: ', task)
# print('After calling loop')

async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url, verify=False)
    return status


def callback(task):
    print('Status:', task.result())


coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
