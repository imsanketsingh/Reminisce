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

    update_query = ""
    if(event):
        update_query = f"UPDATE mytable SET liked = liked + 1 WHERE article = {articleName};"
    else:
        update_query = f"UPDATE mytable SET disliked = disliked + 1 WHERE article = {articleName};"

    cursor.execute(update_query)

    cursor.execute('SELECT * from mytable;')
    updated_rows = cursor.fetchall()
    for row in updated_rows:
        st.markdown(f"{row[1]} has a {row[2]} likes and {row[3]} dislikes")
    
    conn.commit()