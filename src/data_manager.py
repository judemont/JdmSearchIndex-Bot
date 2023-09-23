from src.page_scraper import PageData
import requests
import json

class DataManager:
    def __init__(self, API_BASE_URL: str):
        self.API_BASE_URL = API_BASE_URL

    def save_page_data(self, pdata: PageData):
        postData = {"url": pdata.url, "title": pdata.title, "text": pdata.text, "domain": pdata.domain, "ip": pdata.ip}
        postUrl = self.API_BASE_URL + "save_page_data.php"
        responseJson = requests.post(postUrl, json = postData)
        return False
    
    def is_link_visited(self, url:str):
        postData = {"link": url}
        postUrl = self.API_BASE_URL + "save_page_data.php"
        responseJson = requests.post(postUrl, json = postData)
        # response = json.loads(responseJson)
        # return response["is_link_visited"]
        return False
