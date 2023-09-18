def getLastVisitedUrl(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT URL FROM pages ORDER BY ID DESC LIMIT 1")
    lastUrl = cursor.fetchone()

    if lastUrl == None:
        return False
    else:
        return lastUrl[0]
