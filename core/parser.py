import re
import aiohttp

async def parse_js_for_insights_async(session, url):
    findings = {
        "url": url,
        "imports": set(),
        "fetches": set(),
        "secrets": set(),
        "sourcemaps": set()
    }

    try:
        async with session.get(url, timeout=10) as r:
            content = await r.text()
    except Exception as e:
        print(f"[!] Error fetching JS from {url}: {e}")
        return findings

    findings["imports"] = set(re.findall(r"import\(['\"](.*?)['\"]\)", content))
    findings["fetches"] = set(re.findall(r"(fetch|axios|get|post|put|delete)\(['\"](.*?)['\"]", content))
    findings["secrets"] = set(re.findall(r"(apikey|api_key|secret|token)[\"']?\s*[:=]\s*[\"']([^\"']+)[\"']", content, re.I))
    findings["sourcemaps"] = set(re.findall(r"sourceMappingURL=(.*?\.map)", content))

    findings["fetches"] = {url for method, url in findings["fetches"]}
    findings["secrets"] = {f"{k}={v}" for k, v in findings["secrets"]}

    return findings
