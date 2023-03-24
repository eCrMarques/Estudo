import random
from Dex import Pokedex
class Treinador:
    def __init__(self, nome, dinheiro, pokemons, item=None):
        self.nome = nome
        self.dinheiro = dinheiro
        self.pokemons = pokemons
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
    
    def batalha(self,inimigo):
        pass

class Oponente(Treinador):
    def __init__(self, nome, dinheiro, pokemons):
        super().__init__(nome, dinheiro, pokemons)
    
    def apresentacao(self):
        print(f'Parado ai, Vamos Batalhar\n {self.nome} o Desafiou')


# N=Treinador('a','a','a')
# O=Oponente('Josh',1564,'a')
# print(N.__dict__)
# N.Mochila('a')
# N.Mochila('b')
# print(O.inf())

