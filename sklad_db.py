import sqlite3

conn = sqlite3.connect('sklad.db')
c = conn.cursor()
data = []

c.execute("INSERT INTO items VALUES (8, 'Paul', 32, 'California', 'Хуйзнат');")
conn.commit()
conn.close()
