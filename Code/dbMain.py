import streamlit as st
import mysql.connector

def database(articleName, event):
    host = st.secrets["mysql"]["host"]
    port = st.secrets["mysql"]["port"]
    database = st.secrets["mysql"]["database"]
    username = st.secrets["mysql"]["username"]
    password = st.secrets["mysql"]["password"]

    conn = mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=username,
        password=password
    )

    cursor = conn.cursor()

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

    cursor.close()
    conn.close()
