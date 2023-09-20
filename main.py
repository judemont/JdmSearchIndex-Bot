from src.page_scraper import PageScraper
from src.data_manager import DataManger
import _config as conf

def handlePages(url, dataManager):
    # try:
        page_scrape = PageScraper(url, conf.HEADERS, conf.MAX_PAGE_TEXT_LENGTH).scrape()
        
        print(page_scrape.get_page_data())
        dataManager.save_page_data(page_scrape.get_page_data())

        page_URLs = page_scrape.get_outlinks()
        for pageURL in page_URLs:
            print(pageURL)
            if not dataManager.is_link_visited(pageURL):
                handlePages(pageURL, DataManger)
    # except RecursionError as err:
    #     print(err)
    #     exit();
    # except Exception as err:
    #     print(err)

dataManager = DataManger(conf.API_BASE_URL)

url_to_visit = conf.BASE_URL

handlePages(url_to_visit, dataManager)
