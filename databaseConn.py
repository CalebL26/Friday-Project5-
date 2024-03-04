import sqlite3
connect = sqlite3.connect('FridayProj5.db')
cursor = connect.cursor()

cursor.execute("Select name FROM sqlite_master where type='table';")

tablenames = cursor.fetchall()

for table in tablenames:
    print(table[0])



cursor.execute("SELECT * FROM QuestAns")

rows = cursor.fetchall()

for row in rows:
    print(row)