import sqlite3

def newConnection(SQL_CREATE_TABLE_QUERY):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    cursor.execute(SQL_CREATE_TABLE_QUERY)
    return connection