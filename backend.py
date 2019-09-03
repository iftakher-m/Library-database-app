import sqlite3

def connect():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer) ")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO library VALUES (NULL,?,?,?,?) ", (title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM library")
    rows= cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM library WHERE title=? or author=? or year=? or isbn=?" ,(title,author,year,isbn))
    rows= cur.fetchall()
    conn.close()
    return rows
    
def delete(id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM library WHERE id=?", (id,))
    conn.commit()
    conn.close()
    
def update(id,title,author,year,isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE library SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
# insert('The sun','John mun',4665,235545)
# update(4,"Good life","Stanley clark",3677,3432090)
print(view())
# delete(2)
# print(search(isbn=455))