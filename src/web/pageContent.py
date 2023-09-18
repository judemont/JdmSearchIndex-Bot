from bs4 import BeautifulSoup

def getPageContent(page, MAX_PAGE_TEXT_LENGTH):
    pageSoup = BeautifulSoup(page.content, "html.parser")

    title = pageSoup.find("title")
    description = pageSoup.find("meta")

    if(description == None):
        description = ""
    else:
        description = description.text

    if(title == None):
        title = ""
    else:
        title = title.text


    pageText = pageSoup.get_text(separator="", strip=True)



    pageContent = {}
    pageContent["title"] = title[:255]
    pageContent["description"] = description[:255]
    pageContent["text"] = pageText[:MAX_PAGE_TEXT_LENGTH]
    


    return pageContent

