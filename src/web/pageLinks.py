from bs4 import BeautifulSoup
import validators

def getPageLinks(page):
    pageSoup = BeautifulSoup(page.content, "html.parser")

    links = pageSoup.find_all('a', href=True)
    URLs = []
    for link in links:
        url = link["href"]
        if validators.url(url):
            URLs.append(url)

    return URLs