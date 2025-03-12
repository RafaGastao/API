from flask import Flask,request

app = Flask(__name__)

import sqlite3

# @app.route("/pagar")
# def exibir_mensagem():
#     return "<h1>Pagar as pessoas, faz bem as pessoas!!!</h1>"

# @app.route("/femandaopix")
# def manda_pix():
#     return "<h2>Se a tela apagou, tá devendo!!!<h2>"

# @app.route("/comidas")
# def comida():
#     return "<h2>Tomato á milanesa"

def init_db():
    # sqlite3 crie o arquivo database.db e se conecte com a variável conn (connection)
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
                CREATE TABLE IF NOT EXISTS LIVROS(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     titulo TEXT NOT NULL,
                     categoria TEXT NOT NULL,
                     autor TEXT NOT NULL,
                     imagem_url TEXT NOT NULL
                     )
        """)


init_db()

@app.route("/doar", methods = ["POST"])
def doar(): 

    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados.get("imagem_url")

# Se o arquivo app.py for o arquivo principal da nossa aplicação,
# rode a api no modo de depuração
if __name__ == "__main__":
    app.run(debug=True)