import argparse
import asyncio
import aiohttp
from rich.console import Console
from rich.panel import Panel
from rich import print
from core.crawler import crawl
from core.extractor import extract_js_links
from core.parser import parse_js_for_insights_async

console = Console()

def display_banner(url):
    banner = Panel.fit(
        "[bold white]ShinobiJS[/bold white] 🥷\n[cyan]Silent. Fast. Efficient.[/cyan]",
        border_style="magenta",
        padding=(1, 4),
    )
    console.print(banner)
    print(f"[bold cyan]🔗 Target:[/bold cyan] {url}")

async def analyze_all_js(js_urls):
    dynamic_imports, fetched_endpoints, secrets, sourcemaps = set(), set(), set(), set()
    async with aiohttp.ClientSession() as session:
        tasks = [parse_js_for_insights_async(session, js_url) for js_url in js_urls]
        results = await asyncio.gather(*tasks)

    for findings in results:
        dynamic_imports.update(findings['imports'])
        fetched_endpoints.update(findings['fetches'])
        secrets.update(findings['secrets'])
        sourcemaps.update(findings['sourcemaps'])

    return dynamic_imports, fetched_endpoints, secrets, sourcemaps

async def run(url):
    display_banner(url)
    console.print("[bold yellow]⏳ Crawling pages...[/bold yellow]")
    pages = crawl(url)
    all_js = set()
    inline_scripts = []

    print(f"[bold green]🕸️ Pages Crawled:[/bold green] {len(pages)}")

    for page in pages:
        external, inline = extract_js_links(page)
        all_js.update(external)
        inline_scripts.extend(inline)

    print(f"[bold green]📦 External JS Files Found:[/bold green] {len(all_js)}")
    print(f"[bold green]🧠 Inline Script Blocks Found:[/bold green] {len(inline_scripts)}")

    if not all_js:
        console.print("[bold red]⚠️ No external JS found. Exiting.[/bold red]")
        return

    console.rule("[bold blue]🔍 External JS Files")
    for js in sorted(all_js):
        print(f"[bold green]➤[/bold green] {js}")

    console.print("\n[bold yellow]🔬 Analyzing JS files for endpoints, secrets, and dynamic imports...[/bold yellow]")
    dynamic_imports, fetched_endpoints, secrets, sourcemaps = await analyze_all_js(all_js)

    if dynamic_imports:
        console.rule("[bold magenta]📦 Dynamic Imports")
        for i in sorted(dynamic_imports):
            print(f"[bold cyan]import:[/bold cyan] {i}")

    if fetched_endpoints:
        console.rule("[bold magenta]🌐 Fetched Endpoints")
        for e in sorted(fetched_endpoints):
            print(f"[bold cyan]fetch:[/bold cyan] {e}")

    if secrets:
        console.rule("[bold magenta]🔑 Secrets / Tokens")
        for s in sorted(secrets):
            print(f"[bold red]secret:[/bold red] {s}")

    """if sourcemaps:
        console.rule("[bold magenta]🗺️ Source Maps")
        for m in sorted(sourcemaps):
            print(f"sourcemap:{m}")"""

    console.rule("[bold green]✅ Recon Complete")
    print("[bold green]Stay stealthy, Shinobi. 🥷[/bold green]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ShinobiJS 🥷 - Advanced JS Recon Tool")
    parser.add_argument("url", help="Target base URL")
    args = parser.parse_args()
    asyncio.run(run(args.url))
