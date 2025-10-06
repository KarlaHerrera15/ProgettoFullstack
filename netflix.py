import mysql.connector
import pandas as pd

# Connessione a MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="password123"
)
mycursor = mydb.cursor()

# Creazione del database NETFLIX_DB se non esiste
mycursor.execute("CREATE DATABASE IF NOT EXISTS NETFLIX_DB")

# Seleziona il database
mycursor.execute("USE NETFLIX_DB")

# Creazione della tabella Netflix_Shows con colonne corrette
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Netflix_Shows (
    show_id VARCHAR(20) PRIMARY KEY,
    category VARCHAR(50),
    title VARCHAR(255),
    director VARCHAR(255),
    cast TEXT,
    country VARCHAR(255),
    release_date VARCHAR(50),
    rating VARCHAR(20),
    duration VARCHAR(50),
    type VARCHAR(100),
    description TEXT
);
""")

# Lettura dati dal CSV
netflix_data = pd.read_csv('./netflix_titles.csv')
netflix_data = netflix_data.fillna('Null')  # Rimpiazza valori NaN con 'Null'

# Inserimento dati
cursor = mydb.cursor()
for i, row in netflix_data.iterrows():
    try:
        sql = """
        INSERT INTO Netflix_Shows 
        (show_id, category, title, director, cast, country, release_date, rating, duration, type, description)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            str(row['show_id']),
            row['listed_in'],
            row['title'],
            row['director'],
            row['cast'],
            row['country'],
            row['date_added'],
            row['rating'],
            row['duration'],
            row['type'],
            row['description']
        ))
        print(f"Record {row['show_id']} inserito")
    except mysql.connector.Error as err:
        print(f"Errore inserimento record {row['show_id']}: {err}")

mydb.commit()
cursor.close()

# Verifica dati inseriti
mycursor.execute("SELECT * FROM Netflix_Shows LIMIT 10")
myresult = mycursor.fetchall()
for record in myresult:
    print(record)

