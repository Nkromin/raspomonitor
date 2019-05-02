'''Module needs to be worked on'''
import sqlite3

conn = sqlite3.connect('mark.db')

def get_posts():
	with conn:
		cur.execute("SELECT *FROM ATT")
		print(cur.fetchall())

print("Operation done successfully")
conn.close()
