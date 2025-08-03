import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin


async def fetch_html(session,url):
     try:
          async with session.get(url,timeount=10) as resp:
               return await resp.text()
     except:
          return ""

async def extract_js_links(session,url):
    external = set()
    inline = []

    html = await fetch_html(session,url)
    if not html:
         return external,inline
    soup = BeautifulSoup(html,'html.parser')
    for script in soup.find_all("script"):
        if script.get('scr'):
            js_url = urljoin(url,script['src'])
            if js_url.endswith(".js"):
                external.add(js_url)
            elif script.string:
                 inline.append(script.string)
    
    return external,inline 