import requests

def getPageSource(URL, HEADERS):
    page = requests.get(URL, headers=HEADERS)
    return page