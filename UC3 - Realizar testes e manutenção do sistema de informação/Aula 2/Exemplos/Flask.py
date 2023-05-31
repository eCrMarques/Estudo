from Modelo.classPokemon import *
from Controle.classConexão import *
from flask import Flask, render_template
try:
    db=Conexão("pokemon",'localhost','5432','postgres','postgres')
    Pokemons=db.consultarBanco("""select * from "Pokedex" order by "Número Pokedex" asc """)
except:
    print("erro")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Pokemons" or "/Pokemon")
def Ver():
    return render_template('Pokemons.html',listaPokemons=Pokemons)




if __name__ == "__main__":
    app.run(debug=True, port=5050)