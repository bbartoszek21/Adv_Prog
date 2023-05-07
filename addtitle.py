import sqlite3

conn = sqlite3.connect('books.db')
c = conn.cursor()

c.execute("ALTER TABLE books ADD COLUMN title TEXT")
c.execute("ALTER TABLE books ADD COLUMN author TEXT")
c.execute("ALTER TABLE books ADD COLUMN isbn TEXT")

conn.commit()

conn.close()