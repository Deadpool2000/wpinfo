import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

class WPInfo:
    def __init__(self, url):
        if not url.startswith("http"):
            url = "http://" + url
        self.url = url
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0'})

    def _fetch_html(self, url):
        try:
            res = self.session.get(url, timeout=10)
            res.raise_for_status()
            return res.text
        except Exception:
            return None

    def get_info(self):
        html = self._fetch_html(self.url)
        if not html:
            return {"error": "Failed to fetch site."}

        soup = BeautifulSoup(html, 'html.parser')
        info = {}

        info['title'] = soup.title.string.strip() if soup.title else 'N/A'

        desc = soup.find("meta", attrs={"name": "description"})
        info['meta_description'] = desc['content'] if desc and desc.get('content') else 'N/A'

        generator = soup.find("meta", attrs={"name": "generator"})
        info['wordpress_version'] = generator['content'] if generator else 'Not visible'

        theme_match = re.search(r'/wp-content/themes/([^/]+)/', html)
        info['theme'] = theme_match.group(1) if theme_match else 'Not detected'

        plugins = set(re.findall(r'/wp-content/plugins/([^/]+)/', html))
        info['plugins'] = list(plugins) if plugins else []

        rss_link = soup.find("link", type="application/rss+xml")
        info['rss_feed'] = rss_link['href'] if rss_link and rss_link.get('href') else 'Not found'

        sitemap_url = urljoin(self.url, 'sitemap.xml')
        info['sitemap'] = sitemap_url if self._fetch_html(sitemap_url) else 'Not found'

        robots_url = urljoin(self.url, 'robots.txt')
        info['robots_txt'] = robots_url if self._fetch_html(robots_url) else 'Not found'

        return info
