import sqlite3

class DataBase():
    
    def __init__(self):
        self.createTable()

    def createTable(self):
        connectionDB = sqlite3.connect("database.db")
        cursorDB = connectionDB.cursor()
        cursorDB.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        connectionDB.commit()
        connectionDB.close()

    def insertData(self, title, author, year, isbn):
        connectionDB = sqlite3.connect("database.db")
        cursorDB = connectionDB.cursor()
        cursorDB.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        connectionDB.commit()
        connectionDB.close()

    def viewData(self):
        connectionDB = sqlite3.connect("database.db")
        cursorDB = connectionDB.cursor()
        cursorDB.execute("SELECT * FROM book")
        rows= cursorDB.fetchall()
        connectionDB.close()
        return rows

    def searchData(self, title="", author="", year="", isbn=""):
        connectionDB = sqlite3.connect("database.db")
        cursorDB = connectionDB.cursor()
        cursorDB.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows= cursorDB.fetchall()
        connectionDB.close()
        return rows

    def deleteData(self, id):
        connectionDB = sqlite3.connect("database.db")
        cursorDB = connectionDB.cursor()
        cursorDB.execute("DELETE FROM book WHERE id=?", (id,))
        connectionDB.commit()
        connectionDB.close()

    def updateData(self, id, title, author, year, isbn):
        connectionDB = sqlite3.connect("database.db")
        cursorDB = connectionDB.cursor()
        cursorDB.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        connectionDB.commit()
        connectionDB.close()