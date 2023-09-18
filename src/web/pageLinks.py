from bs4 import BeautifulSoup
import validators
from src.web.urlCleaner import cleanUpUrl

def getPageLinks(page):
    pageSoup = BeautifulSoup(page.content, "html.parser")

    links = pageSoup.find_all('a', href=True)
    URLs = []
    for link in links:
        url = cleanUpUrl(link["href"])
        if validators.url(url):
            URLs.append(url)

    return URLs