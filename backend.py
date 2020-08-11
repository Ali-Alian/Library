 import sqlite3



def connect():

	conn=sqlite3.connect('library.db')
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
	conn.commit()
	conn.close()


def insert(title,author,year,isbn):
	conn=sqlite3.connect('library.db')
	cur=conn.cursor()
	cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
	conn.commit()
	conn.close()


def view():
	conn=sqlite3.connect('library.db')
	cur=conn.cursor()
	cur.execute("SELECT * FROM books")
	rows=cur.fetchall()
	conn.close()
	return rows


def serching(title="",author="",year="",isbn=""):
	conn=sqlite3.connect("library.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
	rows=cur.fetchall()
	conn.close()
	return rows


def delete(id):

	conn = sqlite3.connect("library.db")
	cur= conn.cursor()
	cur.execute("DELETE FROM books WHERE id=?",(id,))	# deleteing the data 
	rows=cur.fetchall()
	conn.commit()
	conn.close()


def update(id,title,author,year,isbn):

	conn = sqlite3.connect("library.db")
	cur= conn.cursor()
	cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))	#updating (price and quantitys) the inserted data 
	rows=cur.fetchall()
	conn.commit()
	conn.close()


connect()
#insert("kirkhar","mamad",1998,23456789)
#delete(3)
#update(3,"bi adab",'asdf',1234,1234)
#print(view())
#print(serching(author="mamad")) 