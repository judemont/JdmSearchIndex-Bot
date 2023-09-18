def isLinkVisited(URL, conn):
    cursor = conn.cursor()

    cursor.execute("SELECT URL FROM pages WHERE URL = ?", (URL,))
    existing_url = cursor.fetchone()

    return not not existing_url
