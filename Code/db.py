import sqlite3
import streamlit as st

def database(articleName, event):
    db_path = 'count.db'
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    # create_table_query = '''
    # CREATE TABLE IF NOT EXISTS mytable (
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # article TEXT NOT NULL,
    # liked INT DEFAULT 0,
    # disliked INT DEFAULT 0
    # );
    # '''

    # cursor.execute(create_table_query)
    articleName_quoted = f"'{articleName}'"

    update_query = ""
    if event:
        update_query = "UPDATE mytable SET liked = liked + 1 WHERE article = ?;"
    else:
        update_query = "UPDATE mytable SET disliked = disliked + 1 WHERE article = ?;"

    cursor.execute(update_query, (articleName,))

    cursor.execute('SELECT * from mytable;')
    updated_rows = cursor.fetchall()
    for row in updated_rows:
        st.markdown(f"{row[1]} has a {row[2]} likes and {row[3]} dislikes")
    
    conn.commit()
    conn.close()