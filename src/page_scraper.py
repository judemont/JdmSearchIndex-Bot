from dataclasses import dataclass
import socket
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import httpx
import validators
from src.utils import cleanup_url

@dataclass
class PageData:
    url: str
    title: str
    description: str
    text: str
    domain: str
    ip: str

class PageScraper:
    def __init__(self, url: str, headers: dict[str, str], max_page_text_length: int) -> None:
        self.url = cleanup_url(url)
        self.headers = headers
        self.max_page_text_length = max_page_text_length
    
    def scrape(self):
        self._download_page_content()
        self._grab_url_domain()
        self._grab_ip()
        return self

    def _process_response(self, response: httpx.Response):
        self.content = response.content
        self.soup = BeautifulSoup(response.content, "html.parser")

    def _download_page_content(self):
        self._process_response(httpx.get(self.url, headers=self.headers, follow_redirects=True))
    
    def _grab_ip(self):
        self.ip = socket.gethostbyname(self.domain)
    
    def _grab_url_domain(self):
        self.domain = urlparse(self.url).netloc

    def get_outlinks(self):
        links = self.soup.find_all('a', href=True)
        URLs = []
        for link in links:
            url = cleanup_url(link["href"])
            if validators.url(url):
                URLs.append(url)

        return URLs
    
    def get_page_data(self):
        title = self.soup.find("title")
        description = self.soup.find("meta")

        description = description.text if description else ""
        title = title.text if title else ""

        page_text = self.soup.get_text(separator="", strip=True)

        return PageData(
            self.url,
            title,
            description,
            page_text,
            self.domain,
            self.ip
        )