import mysql.connector
from flask import Flask, jsonify

# Connessione al database MySQL
mydb = mysql.connector.connect(
  host="localhost",           # Host del database
  user="pythonuser",          # Username MySQL
  password="password123",     # Password MySQL
  database="NETFLIX_DB"       # Nome del database
)
mycursor = mydb.cursor()      # Cursore per eseguire query

app = Flask(__name__)         # Istanza dell'app Flask

# Route per la home page (test)
@app.route("/")
def hello():
    return "Hello, World!"

# Route per mostrare i primi 10 film
@app.route("/first_ten_movies")
def first_ten_movies():
    # Esegue la query per selezionare i primi 10 film
    mycursor.execute("SELECT * FROM Netflix_Shows WHERE type = 'Movie' LIMIT 10")
    columns = [desc[0] for desc in mycursor.description]  # Ottiene i nomi delle colonne
    myresult = mycursor.fetchall()                        # Ottiene i risultati della query
    result = []
    # Trasforma ogni record in un dizionario {colonna: valore}
    for row in myresult:
        result.append(dict(zip(columns, row)))
    return jsonify(result)                                # Restituisce i dati in formato JSON

@app.route("/movies_page/<int:page>")
def movies_page(page):
    per_page = 10  # Numero di film da mostrare per ogni pagina
    offset = (page - 1) * per_page  # Calcola l'offset per la query SQL in base al numero di pagina richiesto
    # Esegue la query per selezionare dieci film in base alla pagina
    mycursor.execute(
        "SELECT * FROM Netflix_Shows WHERE type = 'Movie' LIMIT %s OFFSET %s",
        (per_page, offset)
    )
    columns = [desc[0] for desc in mycursor.description]  # Ottiene i nomi delle colonne della tabella
    myresult = mycursor.fetchall()  # Ottiene i risultati della query
    # Trasforma ogni record in un dizionario {colonna: valore}
    result = [dict(zip(columns, row)) for row in myresult]
    return jsonify(result)  # Restituisce i dati in formato JSON

# Avvia il server Flask in modalità debug
if __name__ == "__main__":
    app.run(debug=True)