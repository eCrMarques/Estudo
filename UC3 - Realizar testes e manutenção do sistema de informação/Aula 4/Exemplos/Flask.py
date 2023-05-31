from Modelo.classPokemon import *
from Controle.classConexão import *
from flask import *
try:
    db=Conexão("pokemon",'localhost','5432','postgres','postgres')
    
except:
    print("erro")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Pokemons", methods=("GET", "POST"))
def Ver():
    Pokemons=db.consultarBanco("""select * from "Pokedex" order by "Número Pokedex" asc """)
    if request.method=="GET":
       return render_template('Pokemons.html',listaPokemons=Pokemons)
    
    elif request.method=="POST":
        resultado=db.manipularBanco(f"""Delete from "Pokedex" where "Número Pokedex"='{request.form["ID"]}' """)
        if resultado:
            return redirect(url_for("Ver"))
        else:
            return "Erro"

@app.route("/Inserir", methods=("GET","POST"))
def inserirPokemons():

    if request.method == "GET":

        return render_template("inserirPokemon.html")
    
    if request.method == "POST":

        
        idPokemon = request.form['ID']
        especiePokemon = request.form['ESPECIE']
        pesoPokemon = request.form['PESO']
        alturaPokemon = request.form['ALTURA']
        tipoPokemon = request.form['TIPO']
        print(idPokemon,especiePokemon,alturaPokemon,pesoPokemon,tipoPokemon)
        resultado = db.manipularBanco(f'''INSERT INTO "Pokedex" values('{idPokemon}','{especiePokemon}','{alturaPokemon}','{pesoPokemon}','{tipoPokemon}','Kanto') ''')

        print(resultado)
        if resultado:
            return redirect(url_for("/Pokemons"))
        else:
            return "Erro na inserção"

@app.route("/Pokemons/<int:idPoke>",methods=("GET","POST"))
def PokemonEspecifico(idPoke):
    Pokemon=db.consultarBanco(f"""select * from "Pokedex" where "Número Pokedex" ='{idPoke}' """)
    if Pokemon and request.method == "POST":
        infoPokemon=[]
        for i,item in enumerate(request.form.keys()):
            if request.form[item]=='':
                infoPokemon.append(Pokemon[0][i])
            else:
                infoPokemon.append(request.form[item])
        
        db.manipularBanco(f"""Update "Pokedex" Set "Número Pokedex" = '{infoPokemon[0]}', "Espécie"= '{infoPokemon[1]}'
        , "Altura" = '{infoPokemon[2]}' , "Peso"='{infoPokemon[3]}' , "Tipo" = '{infoPokemon[4]}' where "Número Pokedex" = '{idPoke}'
        """)
        return redirect(url_for("Ver"))
    if Pokemon and request.method=="GET":
        return render_template("pokemonEspecifico.html",Poke=Pokemon[0])
        
    else:
        "Erro"




if __name__ == "__main__":
    app.run(debug=True, port=5050)