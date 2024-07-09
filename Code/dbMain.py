import streamlit as st
import mysql.connector

def database(articleName, event):
    try:
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
            if existing_row is not None:
                cursor.execute("UPDATE mytable SET liked = liked + 1 WHERE article = ?", (articleName,))
            else:
                cursor.execute("INSERT INTO mytable (article, liked) VALUES (?, 1)", (articleName,))

        else:
            if existing_row is not None:
                cursor.execute("UPDATE mytable SET disliked = disliked + 1 WHERE article = ?", (articleName,))
            else:
                cursor.execute("INSERT INTO mytable (article, disliked) VALUES (?, 1)", (articleName,))

        conn.commit()

    except mysql.connector.Error as err:
        st.error(f"MySQL error: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()