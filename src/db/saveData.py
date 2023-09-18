def savePageData(URL, title, description, text, domain, ip, conn):
    cursor = conn.cursor()

    # Correction : Recherche par l'URL au lieu de l'ID
    cursor.execute("SELECT URL FROM pages WHERE URL = ?", (URL,))
    existing_url = cursor.fetchone()
    
    if not existing_url:
        INSERT_DATA_SQL = """
            INSERT INTO pages (URL, title, description, text, domain, IP) 
            VALUES (?, ?, ?, ?, ?, ?)
        """
        # Utilise des paramètres pour l'insertion de données
        cursor.execute(INSERT_DATA_SQL, (URL, title, description, text, domain, ip))
        conn.commit()
