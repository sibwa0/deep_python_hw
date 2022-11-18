import asyncio
from queue import Queue
import aiohttp
import sys
import time
from collections import Counter
from bs4 import BeautifulSoup
import re

from utils import (
    console_input,
    URLS_TXT
)

def parse_encode_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (
        phrase.strip() for line in lines for phrase in line.split("  ")
    )

    text = '\n'.join(chunk for chunk in chunks if chunk).split()

    return text

async def fetch(session, q: Queue, cnt: Counter):
    while True:
        url = await q.get()

        try:
            async with session.get(url) as resp:
                data = await resp.text()

                text = parse_encode_html(data)

                cnt.update(text)
                print(cnt.most_common(5))
        finally:
            q.task_done()
        

async def batch_fetch(workers, urls):
    q = asyncio.Queue()
    cnt = Counter()

    with open(urls, "r", encoding="utf-8") as fd_urls:
        for url in fd_urls:
            await q.put(url)

    async with aiohttp.ClientSession() as session:
        workers = [
            asyncio.create_task(fetch(session, q, cnt))
            for _ in range(workers)
        ]
        await q.join()
        
        for w in workers:
            w.cancel()

    return cnt


if __name__ == '__main__':
    parser = console_input()
    c_input = parser.parse_args(sys.argv[1:])

    st = time.time()

    cnt_dct = asyncio.run(batch_fetch(c_input.r, c_input.f))
    # cnt_dct = asyncio.run(batch_fetch(10, URLS_TXT))

    end = time.time()
    print(end - st)
    print()
    print(cnt_dct.most_common(10))