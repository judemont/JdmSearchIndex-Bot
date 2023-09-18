from urllib.parse import urlparse, urlunparse

def cleanUpUrl(url):

    parsed_url = urlparse(url)

    netloc = parsed_url.netloc.lstrip("www.")

    path = parsed_url.path.rstrip('/')

    normalized_url = urlunparse(parsed_url._replace(query='', netloc=netloc, path=path))
    
    return normalized_url
