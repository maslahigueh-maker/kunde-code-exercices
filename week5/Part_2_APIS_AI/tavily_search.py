# scripts/tavily_search.py

from urllib.parse import urlparse

from config import TAVILY_API_KEY
from tavily import TavilyClient

client = TavilyClient(api_key=TAVILY_API_KEY)


def _path(url):
    return urlparse(url).path.rstrip("/").lower()


def _has_wanted_page(response, link):
    """True if a returned page is the requested page or sits under it."""
    wanted = _path(link)
    for item in (response or {}).get("results", []):
        got = _path(item.get("url", ""))
        if not wanted or got == wanted or got.startswith(wanted + "/"):
            return True
    return False


def _crawl(link, limit):
    """Start at `link` and follow links one level deep, staying under its path."""
    options = {
        "url": link,
        "max_depth": 1,      # the page itself plus the pages it links to
        "limit": limit,      # hard cap on pages, keeps credits under control
    }

    path = _path(link)
    if path:
        # Only follow pages under the same path (for example /services/crisis/...)
        options["select_paths"] = [path + ".*"]

    return client.crawl(**options)


def search_link(link, crawl=False, limit=8):
    # Follow related pages on the same site
    if crawl:
        try:
            response = _crawl(link, limit)
            if response.get("results"):
                return response
            print(f"  Crawl returned nothing for {link}, using plain extract")
        except Exception as exc:
            print(f"  Crawl failed for {link} ({exc}), using plain extract")

    response = client.extract(urls=link)

    # No matching page came back: retry with the stronger (costlier) mode
    if not _has_wanted_page(response, link):
        response = client.extract(urls=link, extract_depth="advanced")

    return response