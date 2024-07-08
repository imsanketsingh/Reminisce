import sqlite3

conn = sqlite3.connect('count.db')

cursor = conn.cursor()

select_query = '''
    SELECT * FROM mytable;
'''

cursor.execute(select_query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
