from urllib.parse import urlparse

def getUrlDomain(URL):
    domain = urlparse(URL).netloc
    return domain