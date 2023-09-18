import requests

def getPageSource(URL):
    page = requests.get(URL)
    return page
