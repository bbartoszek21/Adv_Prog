import sqlite3

connector = sqlite3.connect('books.db')
cur = connector.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        isbn TEXT
    )
''')

def add(title, author, isbn):
    cur.execute('INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)', (title, author, isbn))
    connector.commit()
    print("Book added.")

def remove(title):
    cur.execute('DELETE FROM books WHERE title = ?', (title,))
    connector.commit()
    print("Book removed.")

def update(title, author, isbn):
    cur.execute('UPDATE books SET author = ?, isbn = ? WHERE title = ?', (author, isbn, title))
    connector.commit()
    print("Book updated.")

def search(title):
    cur.execute('SELECT * FROM books WHERE title = ?', (title,))
    book = cur.fetchone()
    if book:
        print("Book found:")
        print("Title:", book[1])
        print("Author:", book[2])
        print("ISBN:", book[3])
    else:
        print("No result found.")

while True:
    print("\n--- Book Management System ---")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Update a book")
    print("4. Search for a book")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        isbn = input("Enter the ISBN: ")
        add(title, author, isbn)
    elif choice == '2':
        title = input("Enter the book title: ")
        remove(title)
    elif choice == '3':
        title = input("Enter the book title: ")
        author = input("Enter the new author: ")
        isbn = input("Enter the new ISBN: ")
        update(title, author, isbn)
    elif choice == '4':
        title = input("Enter the book title: ")
        search(title)
    elif choice == '5':
        break
    else:
        print("Invalid choice, try again.")

conn.close()
