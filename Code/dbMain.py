import streamlit as st
import mysql.connector

def database(articleName, event):
    
        host = st.secrets["connections.mysql"]["host"]
        port = st.secrets["connections.mysql"]["port"]
        database = st.secrets["connections.mysql"]["database"]
        username = st.secrets["connections.mysql"]["username"]
        password = st.secrets["connections.mysql"]["password"]

        conn = mysql.connector.connect(
            host=host,
            port=port,
            database=database,
            user=username,
            password=password
        )

        cursor = conn.cursor()
        # st.write(articleName)
        # cursor.execute(f"SELECT * FROM mytable WHERE article = {articleName}")
        # existing_row = cursor.fetchone()
        existing_row = None
        if event:
            if existing_row is not None:
                cursor.execute(f"UPDATE mytable SET liked = liked + 1 WHERE article = {articleName}")
            else:
                cursor.execute(f"INSERT INTO mytable (article, liked) VALUES ({articleName}, 1)")

        else:
            if existing_row is not None:
                cursor.execute(f"UPDATE mytable SET disliked = disliked + 1 WHERE article = {articleName}")
            else:
                cursor.execute(f"INSERT INTO mytable (article, disliked) VALUES ({articleName}, 1)")

        conn.commit()

        cursor.close()
        conn.close()

