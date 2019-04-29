import sqlite3

conn = sqlite3.connect('mark.db')
print("Succesful connection")

conn.execute('''CREATE TABLE ATT(NAME TEXT NOT NULL, DATE TEXT NOT NULL);''')
print(" TABle created succewsfully");
conn.close()
