MAX_PAGE_TEXT_LENGTH = 500*1000

SQL_CREATE_TABLE_QUERY = f"""
CREATE TABLE IF NOT EXISTS pages (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    URL varchar(2000),
    title varchar(255),
    description varchar(255),
    text varchar({MAX_PAGE_TEXT_LENGTH}),
    domain varchar(255),
    IP varchar(255)
);
"""

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
    "Referer": "http://www.google.com/"
}

BASE_URL = "https://rmbi.ch/jdm"