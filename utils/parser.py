import re 
import aiohttp

async def fetch_js(session,url):
     try:
          async with session.get(url,timeount=10) as resp:
               return await resp.text()
     except:
          return ""

async def parse_js(session,js_url):
        js = await fetch_js(session,js_url)
        imports = re.findall(r'import\((["\'])(.*?)\1\)', js)
        fetches = re.findall(r'(fetch|axios\\.get|axios\\.post)\\((["\'])(.*?)\\2', js)
        secrets = re.findall(r'(apikey|token|secret)[\\s]*[:=][\\s]*[\"\\\']?([A-Za-z0-9-_]{10,})', js)
        sourcemaps = re.findall(r'sourceMappingURL=([\\w./\\-]+\\.map)', js)

        return {
        "url": js_url,
        "imports": [i[1] for i in imports],
        "fetches": [f[2] for f in fetches],
        "secrets": [f"{k}={v}" for k, v in secrets],
        "sourcemaps": sourcemaps
        }