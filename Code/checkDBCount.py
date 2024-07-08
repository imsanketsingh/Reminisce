import sqlite3

# Connect to SQLite database (creates a new file if not exists)
conn = sqlite3.connect('count.db')  # Replace 'your_database.db' with your actual database file

# Create a cursor object using the connection
cursor = conn.cursor()

# SQL query to select all entries from mytable
select_query = '''
    SELECT * FROM mytable;
'''

# Execute the query
cursor.execute(select_query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
