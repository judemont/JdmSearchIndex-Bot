from src.web import pageContent as pContent, pageSource, pageLinks, urlDomain, domainIp
from src.db import connection, saveData, linkVisited, lastVisitedLink
import _config as conf




def handlePages(URL, conn):
    try:
        print(URL)

        page = pageSource.getPageSource(URL)
        pageContent = pContent.getPageContent(page, conf.MAX_PAGE_TEXT_LENGTH)
        domain = urlDomain.getUrlDomain(URL)
        IP = domainIp.getIp(domain)

        saveData.savePageData(URL, pageContent["title"], pageContent["description"], pageContent["text"], domain, IP, conn)

        pageURLs = pageLinks.getPageLinks(page)

        for pageURL in pageURLs:
            if not linkVisited.isLinkVisited(pageURL, conn):
                handlePages(pageURL, conn)
    except Exception as err:
        print(err)



conn = connection.newConnection(conf.SQL_CREATE_TABLE_QUERY)
lastVisitedLink = lastVisitedLink.getLastVisitedUrl(conn)
if not lastVisitedLink:
    urlToVisit = "https://rmbi.ch/jdm"
else:
    urlToVisit = lastVisitedLink

handlePages(urlToVisit, conn)