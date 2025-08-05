import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from collections import deque

def crawl(base_url, max_depth=2):
    visited = set()
    queue = deque([(base_url, 0)])
    found = set()
    domain = urlparse(base_url).netloc

    while queue:
        url, depth = queue.popleft()
        if url in visited or depth > max_depth:
            continue
        visited.add(url)
        try:
            response = requests.get(url, timeout=10)
            found.add(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for tag in soup.find_all("a", href=True):
                link = urljoin(url, tag['href'])
                if domain in link:
                    queue.append((link, depth + 1))
        except Exception:
            pass
    return found
