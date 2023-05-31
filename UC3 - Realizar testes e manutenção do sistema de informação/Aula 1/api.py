import requests
import json
lista=[]
def adicionar(pokemon):
    with open ("Pokemon.json","w") as arquivo:
        global lista
        poke={}
        poke["Nome"]=pokemon[0]
        poke["tipos"]=pokemon[1]
        lista.append(poke)

        json.dump(lista,arquivo)
with open ("Pokemon.json","r") as arquivo:
    Pokemon=json.load(arquivo)
    for i in range(151):
        print(Pokemon[i+1]["Nome"])
# for i in range(151):
#     segundoTipo=[]
#     poke = requests.get(f"http://pokeapi.co/api/v2/pokemon/{i+1}")
#     pokeDict=poke.json()
#     segundoTipo.append(pokeDict["types"][0]["type"]["name"])
#     if len(pokeDict["types"])>1:
#         segundoTipo.append(pokeDict["types"][1]["type"]["name"])
#     adicionar((pokeDict["name"],segundoTipo))