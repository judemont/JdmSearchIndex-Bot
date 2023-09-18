import sqlite3

class DbManager:
    INSERT_DATA_SQL = """
        INSERT INTO pages (URL, title, description, text, domain, IP) 
        VALUES (?, ?, ?, ?, ?, ?)
    """

    def __init__(self, sql_create_table_query: str, filename: str = "data.db") -> None:
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql_create_table_query)
    
    def get_last_visited_url(self):
        last_url = self.cursor.execute("SELECT URL FROM pages ORDER BY ID DESC LIMIT 1").fetchone()
        
        return last_url if last_url else False

    def is_link_visited(self, url):
        # modified behavior: not not removed
        return self.cursor.execute("SELECT URL FROM pages WHERE URL = ?", (url,)).fetchone()
    
    def save_page_data(self, url, title, description, text, domain, ip):
        if not self.is_link_visited(url):
            self.cursor.execute(self.INSERT_DATA_SQL, (url, title, description, text, domain, ip))
            self.connection.commit()
