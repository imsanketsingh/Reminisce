import pymysql
import streamlit as st

def database(articleName, event):

    timeout = 10
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db= st.secrets["mysql"]["database"],
        host= st.secrets["mysql"]["host"],
        password= st.secrets["mysql"]["password"],
        read_timeout=timeout,
        port=st.secrets["mysql"]["port"],
        user= st.secrets["mysql"]["user"],
        write_timeout=timeout,
    )
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM mytable WHERE article = %s", (articleName,))
        existing_row = cursor.fetchone()
        if event:
            if existing_row is not None:
                cursor.execute("UPDATE mytable SET liked = liked + 1 WHERE article = %s", (articleName,))
            else:
                cursor.execute("INSERT INTO mytable (article, liked) VALUES (%s, 1)", (articleName,))
        else:
            if existing_row is not None:
                cursor.execute("UPDATE mytable SET disliked = disliked + 1 WHERE article = %s", (articleName,))
            else:
                cursor.execute("INSERT INTO mytable (article, disliked) VALUES (%s, 1)", (articleName,))
        connection.commit()
    finally:
        connection.close()