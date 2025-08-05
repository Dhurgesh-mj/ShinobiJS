from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import requests

def extract_js_links(url):
    external_js = set()
    inline_scripts = []

    try:
        r = requests.get(url, timeout=10)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')

        for script in soup.find_all("script"):
            src = script.get("src")
            if src and ".js" in src:
                full_src = urljoin(url, src)
                external_js.add(full_src)
            elif script.string:
                inline_scripts.append(script.string)
        pattern = r"""(?:"|')((?:https?:)?//[^"']+\.js(?:\?[^"']*)?)(?:"|')"""
        found = re.findall(pattern, html)
        external_js.update(found)

    except Exception as e:
        print(f"[!] Failed to extract from {url}: {e}")

    return external_js, inline_scripts
