import argparse
import aiohttp
import asyncio
from utils.crawler import crawl 
from utils.extractor import extract_js_links
from utils.parser import parse_js

async def analyze_all_js(js_urls):
    dynamic_imports,fetched_endpoint,secrets,sourcemaps = set(),set(),set(),set()
    async with aiohttp.ClientSession() as session:
        task = [parse_js(session,js_url) for js_url in js_urls]
        result = await asyncio.gather(*task)

    for findings in result :
        dynamic_imports.update(findings['imports'])
        fetched_endpoint.update(findings['fetches'])
        secrets.update(findings['secrets'])
        sourcemaps.update(findings['sourcemaps'])

    return dynamic_imports,fetched_endpoint,secrets,sourcemaps

def run(url):
    pages  = crawl(url)