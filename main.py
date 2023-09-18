from src.web import pageContent as pContent, pageSource, pageLinks, urlDomain, domainIp, urlCleaner
from db_manager import DbManager
import _config as conf

def handlePages(url, db_manager: DbManager):
    try:
        cleanedUrl = urlCleaner.cleanUpUrl(url)
        print(cleanedUrl)
        page = pageSource.getPageSource(cleanedUrl, conf.HEADERS)
        pageContent = pContent.getPageContent(page, conf.MAX_PAGE_TEXT_LENGTH)
        domain = urlDomain.getUrlDomain(cleanedUrl)
        IP = domainIp.getIp(domain)

        db_manager.save_page_data(cleanedUrl, pageContent["title"], pageContent["description"], pageContent["text"], domain, IP)

        pageURLs = pageLinks.getPageLinks(page)

        for pageURL in pageURLs:
            if not db_manager.is_link_visited(pageURL):
                handlePages(pageURL, db_manager)
    except Exception as err:
        print(err)

db_manager = DbManager(conf.SQL_CREATE_TABLE_QUERY)

last_visited_link = db_manager.get_last_visited_url()

url_to_visit = last_visited_link if last_visited_link else conf.BASE_URL

handlePages(url_to_visit, db_manager)
