import time, random
from Dex import Pokedex
def printLento(texto,velocidadeDotexto=0.1):
    for x in texto:
        print(x,end='',flush=True)
        time.sleep(velocidadeDotexto)

def apagar(b):
    a=' '*(len(b))
    printLento(f'\r{a}')

def Loading(load,velocidadeDotexto,qntd):
        a='/'*(len(load))
        printLento(f'[{load}]',0.001)
        printLento(f'\r[{a}]')
        printLento(f'\r[{load}]')
        
class Pokemon:
    def __init__(self, nome, tipo, hp, atk, df, spd):
        self.nome=nome
        self.tipo=tipo
        self.hp=hp
        self.atk=atk
        self.df=df
        self.spd=spd
    
    def Aleatorio(selvagens):
        Aleatorio=Pokedex.index(random.choice(selvagens))
        return Pokemon(Pokedex[Aleatorio],Pokedex[Aleatorio+1]['tipo'],Pokedex[Aleatorio+1]['Hp'],Pokedex[Aleatorio+1]['Atk'],Pokedex[Aleatorio+1]['Def'],Pokedex[Aleatorio+1]['Speed'])

class Treinador:
    def __init__(self, nome, dinheiro, pokemons, item=None):
        self.nome = nome
        self.dinheiro = dinheiro
        if type(pokemons)!=tuple or len(pokemons)<=6 :
            self.pokemons=pokemons
        else:
            self.pokemons=pokemons[0:6]
            print('Limite Atingido')
        if item==None:
            self.item=[]
        else:
            self.item =item

# pokemon1 =Pokemon(Pokedex[0],Pokedex[1]['tipo'],Pokedex[1]['Hp'],Pokedex[1]['Atk'],Pokedex[1]['Def'],Pokedex[1]['Speed'])
# pokemon2 =Pokemon(Pokedex[4],Pokedex[5]['tipo'],Pokedex[5]['Hp'],Pokedex[5]['Atk'],Pokedex[5]['Def'],Pokedex[5]['Speed'])
# Eu=Treinador('Leo',1654,(pokemon1))

# print(Eu.pokemons)
x=random.randrange(0,6,2)
pokemon1=Pokemon(Pokedex[x],Pokedex[x+1]['tipo'],Pokedex[x+1]['Hp'],Pokedex[x+1]['Atk'],Pokedex[x+1]['Def'],Pokedex[x+1]['Speed'])
print(pokemon1.__dict__)
# Loading('.....Carregando.....')
selvagem=Pokemon.Aleatorio(('Mankey','Oddish','Vileplume'))
print(selvagem.__dict__)