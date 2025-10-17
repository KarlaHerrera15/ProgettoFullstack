import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS

# Connessione al database MySQL
mydb = mysql.connector.connect(
  host="localhost",           
  user="pythonuser",         
  password="password123",     
  database="NETFLIX_DB"      

mycursor = mydb.cursor()     
app = Flask(__name__)         
CORS(app)                   

# Route per la home page (test)
@app.route("/")
def hello():
    return "Hello, World!"

# Route per mostrare i primi 10 film
@app.route("/first_ten_movies")
def first_ten_movies():
    # Esegue la query per selezionare i primi 10 film
    mycursor.execute("SELECT * FROM Netflix_Shows WHERE type = 'Movie' LIMIT 10")
    columns = [desc[0] for desc in mycursor.description]  
    myresult = mycursor.fetchall()                       
    result = []
    # Trasforma ogni record in un dizionario {colonna: valore}
    for row in myresult:
        result.append(dict(zip(columns, row)))
    return jsonify(result)                                

@app.route("/movies_page/<int:page>")
def movies_page(page):
    per_page = 10  
    offset = (page - 1) * per_page  
    # Esegue la query per selezionare dieci film in base alla pagina
    mycursor.execute(
        "SELECT * FROM Netflix_Shows WHERE type = 'Movie' LIMIT %s OFFSET %s",
        (per_page, offset)
    )
    columns = [desc[0] for desc in mycursor.description]  
    myresult = mycursor.fetchall()  
    # Trasforma ogni record in un dizionario {colonna: valore}
    result = [dict(zip(columns, row)) for row in myresult]
    return jsonify(result)  
    
# Avvia il server Flask in modalità debug
if __name__ == "__main__":
    app.run(debug=True)