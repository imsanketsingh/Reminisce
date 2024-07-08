import sqlite3
import streamlit as st

def database(articleName, event):
    db_path = 'D:\Documents\Reminisce\count.db'
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

    cursor.execute("SELECT * FROM mytable WHERE article = ?", (articleName,))
    existing_row = cursor.fetchone()

    if event:
        if existing_row:
            cursor.execute("UPDATE mytable SET liked = liked + 1 WHERE article = ?", (articleName,))
        else:
            cursor.execute("INSERT INTO mytable (article, liked) VALUES (?, 1)", (articleName,))

    else:
        if existing_row:
            cursor.execute("UPDATE mytable SET disliked = disliked + 1 WHERE article = ?", (articleName,))
        else:
            cursor.execute("INSERT INTO mytable (article, disliked) VALUES (?, 1)", (articleName,))
    
    conn.commit()
    conn.close()