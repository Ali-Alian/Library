import sqlite3


class Database:

	def __init__(self, db):

		self.conn=sqlite3.connect(db)
		self.cur=self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
		self.conn.commit()
		


	def insert(self,title,author,year,isbn):
		
		self.cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
		self.conn.commit()
		#self.conn.close()


	def view(self):
		
		self.cur.execute("SELECT * FROM books")
		rows=self.cur.fetchall()
		#self.conn.close()
		return rows
	

	def serching(self,title="",author="",year="",isbn=""):
		
		self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
		rows=self.cur.fetchall()
		#conn.close()
		return rows


	def delete(self,id):

		self.cur.execute("DELETE FROM books WHERE id=?",(id,))	# deleteing the data 
		rows=self.cur.fetchall()
		self.conn.commit()



	def update(self,id,title,author,year,isbn):

		self.cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))	#updating (price and quantitys) the inserted data 
		rows=self.cur.fetchall()
		self.conn.commit()
		#conn.close()

	def __del__(self):
		self.conn.close()

 