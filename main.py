from src.page_scraper import PageScraper
from src.db_manager import DbManager

import _config as conf

def handlePages(url, db_manager: DbManager):
    try:
        page_scrape = PageScraper(url, conf.HEADERS, conf.MAX_PAGE_TEXT_LENGTH).scrape()
        
        print(page_scrape.url)
        
        db_manager.save_page_data(page_scrape.get_page_data())

        page_URLs = page_scrape.get_outlinks()
        for pageURL in page_URLs:
            if not db_manager.is_link_visited(pageURL):
                handlePages(pageURL, db_manager)
        
    except Exception as err:
        print(err)

db_manager = DbManager(conf.SQL_CREATE_TABLE_QUERY)

last_visited_link = db_manager.get_last_visited_url()

url_to_visit = last_visited_link if last_visited_link else conf.BASE_URL

handlePages(url_to_visit, db_manager)
