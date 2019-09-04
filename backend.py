import sqlite3

class Database:

    def __init__(self, db): # if "self" isn't written, "database" object from 'frontend' will be passsed there.  
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()  # 'self' to make 'cur' an attribute of 'database' object and later use in other functions.
        self.cur.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer) ")
        self.conn.commit()
       

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO library VALUES (NULL,?,?,?,?) ", (title,author,year,isbn))
        self.conn.commit()
        

    def view(self):
        self.cur.execute("SELECT * FROM library")
        rows= self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM library WHERE title=? or author=? or year=? or isbn=?" ,(title,author,year,isbn))
        rows= self.cur.fetchall()
        return rows
        
    def delete(self,id):
        self.cur.execute("DELETE FROM library WHERE id=?", (id,))
        self.conn.commit()
        
        
    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE library SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()
        
    def __del__(self):   # Delete the object when the script is discarded, similar to 'destructor', not mandatory to use.
        self.conn.close()

# connect()
# insert('The sun','John mun',4665,235545)
# update(4,"Good life","Stanley clark",3677,3432090)
# print(view())
# delete(2)
# print(search(isbn=455))