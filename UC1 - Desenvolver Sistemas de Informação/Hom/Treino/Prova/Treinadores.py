from Pokemon import *
from Textos import *
from testes import *

class Treinador:
    def __init__(self, nome, pokemons, dinheiro):
        self.nome=nome
        self.pokemons=[].append(pokemons)
        self.dinheiro=dinheiro
    
    def batalha(self,oponente):
        total=self.pokemons.hp
        totalO=oponente.pokemons.hp
        if self.pokemons.spd>=oponente.pokemons.spd:
            primeiro=self.pokemons
            segundo=oponente.pokemons
        else:
            primeiro=oponente.pokemons
            segundo=self.pokemons
        
        while True:
            print(f'{self.nome}\t\t\t\t\t\t {oponente.nome}\n'
                  f'{self.pokemons.nome} Vida {primeiro.hp}\t\t {oponente.pokemons.nome} Vida {segundo.hp}\n')
            if primeiro.hp<=0:
                print(segundo.nome,'Win')
                break
            elif segundo.hp<=0:
                print(primeiro.nome,'Win')
                break
            if primeiro==self.pokemons and segundo.hp>=int(primeiro.atk/10):
                print(f'Seu {primeiro.nome} Esta Pronto Para a Batalha')
                if OpçõesLuta():
                    print(f'Seu {primeiro.nome} Ataca o {segundo.nome}')
                    segundo.hp-=int(primeiro.atk/10)
                    print(f'{segundo.nome} Ataca seu {primeiro.nome}')
                    primeiro.hp-=int(segundo.atk/10)
            else:
                print(f'{segundo.nome} Ataca seu {primeiro.nome}')
                primeiro.hp-=int(segundo.atk/10)
                print(f'Seu {primeiro.nome} Esta Pronto Para a Batalha')
                if OpçõesLuta():
                    print(f'Seu {primeiro.nome} Ataca o {segundo.nome}')
                    segundo.hp-=int(primeiro.atk/10)
                      


class Jogador(Treinador):
    def __init__(self, nome, pokemons, dinheiro):
        super().__init__(nome, pokemons, dinheiro)
        self.pokemons=pokemons

    def batalha(self,oponente):
        return super().batalha(oponente)


class Oponente(Treinador):
    def __init__(self, nome, pokemons, dinheiro):
        super().__init__(nome, pokemons, dinheiro)
        self.pokemons=pokemons

eu=Jogador('Emanuel',Selvagem('FIRE'),654)
npc=Oponente('ash',Selvagem('WATER'),1564)

eu.batalha(npc)