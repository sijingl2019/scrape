import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center')
    await page.waitForSelector('.item .name')
    doc = pq(await page.content())
    names = [item.text() for item in doc('.item .name').items()]

    print('Names: ', names)
    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
