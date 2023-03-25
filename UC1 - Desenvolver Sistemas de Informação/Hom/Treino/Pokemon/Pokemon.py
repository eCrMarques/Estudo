import random
from Dex import Pokedex,Lento

        

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
    
    def Mochila(self,item=None):
        if item!=None:
            self.item.append(item)
        else:
            pass
        print(self.item)
    
    def batalha(self, pokemon,inimigo):
        print(pokemon.spd,inimigo.spd)

class Oponente():
    def __init__(self, nome, dinheiro, pokemons):
        super().__init__(nome, dinheiro, pokemons)
    
    def Pokemon(self, nome, tipo, hp, atk, df, spd):
        super(Pokemon).__init__(nome,tipo, hp, atk, df, spd)

    def apresentacao(self):
        print(f'Parado ai, Vamos Batalhar\n {self.nome} o Desafiou')


class Pokemon(Treinador):
    def Aleatorio(selvagens):
        Aleatorio=Pokedex.index(random.choice(selvagens))
        return Pokemon(Pokedex[Aleatorio],Pokedex[Aleatorio+1]['tipo'],Pokedex[Aleatorio+1]['Hp'],Pokedex[Aleatorio+1]['Atk'],Pokedex[Aleatorio+1]['Def'],Pokedex[Aleatorio+1]['Speed'])

    def __init__(self, nome, tipo, hp, atk, df, spd):
        self.nome=nome
        self.tipo=tipo
        self.hp=hp
        self.atk=atk
        self.df=df
        self.spd=spd

    def stats(self, nome, tipo, hp, atk, df, spd):
        return super().batalha(nome, tipo, hp, atk, df, spd)
        

pokemon1=Pokemon.Aleatorio(('Bulbasaur','Charmander','Squirtle'))
pokemon2=Pokemon.Aleatorio(('Bulbasaur','Charmander','Squirtle'))
Eu=Treinador('Leo',1654,(pokemon1))


Eu.batalha(pokemon1,pokemon2)








# N=Treinador('a','a','a')
# O=Oponente('Josh',1564,'a')
# print(N.__dict__)
# N.Mochila('a')
# N.Mochila('b')
# print(O.inf())

