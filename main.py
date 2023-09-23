from src.page_scraper import PageScraper
from src.data_manager import DataManager
import _config as conf

def handle_pages(url, data_manager):
    try:
        page_scrape = PageScraper(url, conf.HEADERS, conf.MAX_PAGE_TEXT_LENGTH).scrape()

        print(page_scrape.get_page_data())
        data_manager.save_page_data(page_scrape.get_page_data())

        page_URLs = page_scrape.get_outlinks()
        for pageURL in page_URLs:
            print(pageURL)
            if not data_manager.is_link_visited(pageURL):
                handle_pages(pageURL, data_manager)
    except RecursionError as err:
        print(err)
        exit()
    except Exception as err:
        print(err)

data_manager = DataManager(conf.API_BASE_URL)

url_to_visit = conf.BASE_URL

handle_pages(url_to_visit, data_manager)
