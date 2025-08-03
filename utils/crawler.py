import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse
from collections import deque

async def fetch_html(session,url):
     try:
          async with session.get(url,timeount=10) as resp:
               return await resp.text()
     except:
          return ""


async def crawl(base_url,max_depth=2):
     visited,queue,found = set(),deque([(base_url,0)]),set()
     domian = urlparse(base_url).netloc

     async with aiohttp.ClientSession() as session:
          while queue:
               url ,depth = queue.popleft()
               if url in visited or depth > max_depth:
                         continue
               visited.add(url)
               html = await fetch_html(session,url)
               if not html :
                     continue
               found.add(url)
               soup = BeautifulSoup(html,'html.paser')
               for tag  in soup.find_all("a",href=True):
                     link = urljoin(url,tag['href'])
                     if domian in link and link not in visited:
                           queue.append((link,depth+1))
     return found



