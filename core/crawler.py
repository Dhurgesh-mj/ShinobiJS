import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return url, await response.text()
    except:
        return url, None

async def crawl_async(base_url, max_depth=2):
    visited = set()
    queue = deque([(base_url, 0)])
    found = set()
    domain = urlparse(base_url).netloc

    connector = aiohttp.TCPConnector(limit=0)
    headers = {"User-Agent": "Mozilla/5.0 (ShinobiJS Recon Tool)"}
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        while queue:
            tasks = []
            while queue:
                url, depth = queue.popleft()
                if url not in visited and depth <= max_depth:
                    visited.add(url)
                    tasks.append(asyncio.create_task(fetch(session, url))) 

            results = await asyncio.gather(*tasks)
            for url, html in results:
                if html:
                    found.add(url)
                    soup = BeautifulSoup(html, 'html.parser')
                    for tag in soup.find_all("a", href=True):
                        link = urljoin(url, tag['href'])
                        if domain in link and link not in visited:
                            queue.append((link, depth + 1))
    return found
