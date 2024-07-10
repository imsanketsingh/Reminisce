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

        counts = [0,0]

        cursor = conn.cursor()
        # st.write(articleName)
        cursor.execute(f"SELECT * FROM mytable WHERE article = %s", (articleName,))
        existing_row = cursor.fetchone()
        
        if event:
            if existing_row is not None:
                cursor.execute("UPDATE mytable SET liked = liked + 1 WHERE article = %s", (articleName,))
                counts[0] = existing_row[2]
                counts[1] = existing_row[3]
                # st.write(1)
            else:
                cursor.execute("INSERT INTO mytable (article, liked) VALUES (%s, 1)", (articleName,))
                counts[0] = 1
                # st.write(2)
        else:
            if existing_row is not None:
                cursor.execute("UPDATE mytable SET disliked = disliked + 1 WHERE article = %s", (articleName,))
                counts[0] = existing_row[2]
                counts[1] = existing_row[3]
                # st.write(3)
            else:
                cursor.execute("INSERT INTO mytable (article, disliked) VALUES (%s, 1)", (articleName,))
                counts[1] = 1
                # st.write(4)

        conn.commit()

        cursor.close()
        conn.close()

        return counts

    except mysql.connector.Error as e:
        # st.error(f"Error: {e}")
        return ["NA", "NA"]
    except Exception as e:
        # st.error(f"Unexpected error: {e}")
        return ["NA", "NA"]
