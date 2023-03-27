import random
from Dex import *

class Treinador:
    def __init__(self, nome, dinheiro, pokemons, item=None):
        self.nome = nome
        self.dinheiro = dinheiro
        if type(pokemons)!=list or len(pokemons)<=6 :
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

    def Capturar(self, pokemon):
        if len(self.pokemons)<6:
            self.pokemons.append(pokemon)
            print(len(self.pokemons))
        else:
            print('O pokemon foi pro centro Pokemons')
    
    def batalha(self,inimigo):
        if type(self.pokemons)==tuple:
            self.pokemons=self.pokemons[0]
        else:
            pass
        if self.pokemons.spd>=inimigo.pokemons.spd:
            primeiro=self.pokemons      
            segundo=inimigo.pokemons
        else:
            primeiro=inimigo.pokemons
            segundo=self.pokemons
        while True:
            if primeiro ==self.pokemons and segundo.hp>(primeiro.atk/10) and segundo.hp>0:
                if int(input(f"{primeiro.nome} Vida: {int(primeiro.hp)}\n(1) Atacar\n(2) Fugir\n"))==1:
                    segundo.hp-=primeiro.atk/10
                    print(f'\t\t\t{primeiro.nome} Atacou {segundo.nome}\n{segundo.nome} Vida Restante: {int(segundo.hp)}')
                    
                primeiro.hp-=segundo.atk/10
                print(f'\t\t\t{segundo.nome} Atacou {primeiro.nome}')
            elif primeiro !=self.pokemons and primeiro.hp>(segundo.atk/10) and primeiro.hp>0:
                primeiro.hp-=segundo.atk/10
                print(f'\t\t\t{segundo.nome} Atacou {primeiro.nome}')
                if int(input(f"{primeiro.nome} Vida: {int(primeiro.hp)}\n(1) Atacar\n(2) Fugir\n"))==1:
                    segundo.hp-=primeiro.atk/10
                    print(f'\t\t\t{primeiro.nome} Atacou {segundo.nome}\n{segundo.nome} Vida Restante: {int(segundo.hp)}')
        
            else:
                if primeiro.hp>=0:
                    print(segundo.nome,'Win')
                    break
                elif segundo.hp>=0:
                    print(primeiro.nome,'Win')
                    break

class Oponente(Treinador):
    def __init__(self, nome, dinheiro, pokemons):
        super().__init__(nome, dinheiro, pokemons)
    
    def Pokemon(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome,tipo, hp, atk, df, spd)

    def apresentacao(self):
        print(f'Parado ai, Vamos Batalhar\n {self.nome} o Desafiou')

class Pokemon:
    def Aleatorio(selvagens):
        Aleatorio=Pokedex.index(random.choice(selvagens))
        return Pokemon(Pokedex[Aleatorio],Pokedex[Aleatorio+1]['tipo'],Pokedex[Aleatorio+1]['Hp'],Pokedex[Aleatorio+1]['Atk'],Pokedex[Aleatorio+1]['Def'],Pokedex[Aleatorio+1]['Speed'])

    def __init__(self, nome, tipo, hp, atk, df, spd, apelido=None):
        self.nome=nome
        self.tipo=tipo
        self.hp=hp
        self.atk=atk
        self.df=df
        self.spd=spd
        if apelido!=None:
            self.nome=apelido
    def stats(self, nome, tipo, hp, atk, df, spd):
        return super().batalha(nome, tipo, hp, atk, df, spd)
        









poke=Pokedex.index('Bulbasaur')
pokemon1=Pokemon(Pokedex[poke],Pokedex[poke+1]['tipo'],Pokedex[poke+1]['Hp'],Pokedex[poke+1]['Atk'],Pokedex[poke+1]['Def'],Pokedex[poke+1]['Speed'])
def Aleatorio():
    return Pokemon.Aleatorio((TodosPokemons()))
Eu=Treinador('Leo',1654,[pokemon1])
Eu.Capturar(Aleatorio())
Eu.Capturar(Aleatorio())
Eu.Capturar(Aleatorio())
Eu.Capturar(Aleatorio())
Eu.Capturar(Aleatorio())
Eu.Capturar(Aleatorio())



Npc= Oponente('Ash',1564,pokemon1)


# Eu.batalha(Npc)








# N=Treinador('a','a','a')
# O=Oponente('Josh',1564,'a')
# print(N.__dict__)
# N.Mochila('a')
# N.Mochila('b')
# print(O.inf())

