import random
from Dex import *

def aleatorio(classe,tipo):
    aleatorio=random.choice(pokemonstipo(tipo))
    local =Pokedex.index(aleatorio)
    return classe(Pokedex[local],'',Pokedex[local+1]['Hp'],Pokedex[local+1]['Atk'],Pokedex[local+1]['Def'],Pokedex[local+1]['Speed'])


# class Treinador:
#     def __init__(self, nome, pokemons, dinheiro):
#         self.nome=nome
#         self.pokemons=pokemons
#         self.dinheiro=dinheiro
    
#     def batalha(self,jogador,oponente):
#         print(jogador,oponente.pokemons)

# class Jogador(Treinador):
#     def __init__(self, nome, pokemons, dinheiro):
#         super().__init__(nome, pokemons, dinheiro)
#     def batalha(self,oponente):
#         return super().batalha(self.pokemons,oponente)

# class Oponente(Treinador):
#     def __init__(self, nome, pokemons, dinheiro):
#         super().__init__(nome, pokemons, dinheiro)

    
class Pokemon:
    def __init__(self, nome, tipo, hp, atk, df, spd):
        self.nome=nome
        self.tipo=tipo
        self.hp=hp
        self.atk=atk
        self.df=df
        self.spd=spd
        self.movimentos=[]
        self.vantagem=[]    
        self.desvantagem=[]
    
    def batalhar(self):
        pass

    def checarVantagem(self, oponente):
        if oponente.tipo in self.vantagem:
            return 2
        elif oponente.tipo in self.desvantagem:
            return 0.5
        else:
            return 1
        
class PokemonFogo(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Fogo'
        self.movimentos=[]
        self.vantagem=['Inseto','Planta',]
        self.desvantagem=['Pedra','Terrestre','Agua']

class PokemonAgua(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Agua'
        self.movimentos=[]
        self.vantagem=['Fogo','Terrestre','Pedra']
        self.desvantagem=['Elétrico ','Planta']

class PokemonPlanta(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Planta'
        self.movimentos=[]
        self.vantagem=['Terrestre','Pedra ','Água']
        self.desvantagem=['Inseto','Fogo','Voador']

class PokemonEletrico(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Eletrico'
        self.movimentos=[]
        self.vantagem=['Água ','Voador']
        self.desvantagem=['Terrestre']

class PokemonVoador(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Voador'
        self.movimentos=[]
        self.vantagem=['Inseto','Lutador','Planta']
        self.desvantagem=['Elétrico','Pedra']

class PokemonPedra(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Pedra'
        self.movimentos=[]
        self.vantagem=['Inseto','Fogo ','Voador ']
        self.desvantagem=['Planta','Terrestre','Água']
    
class PokemonInseto(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Inseto'
        self.movimentos=[]
        self.vantagem=['Planta ',]
        self.desvantagem=['Fogo','Voador ','Pedra']

class PokemonNormal(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Normal'
        self.movimentos=[]
        self.vantagem=['Lutador']
        self.desvantagem=['Fantasma']

class PokemonTerrestre(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Terrestre'
        self.movimentos=[]
        self.vantagem=[]
        self.desvantagem=[]

class PokemonVenenoso(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Venenoso'
        self.movimentos=[]
        self.vantagem=[]
        self.desvantagem=[]


def Selvagem(tipo):
    match tipo:
        case 'GRASS':
            return aleatorio(PokemonPlanta,'GRASS')
        case 'FIRE':
            return aleatorio(PokemonFogo,'FIRE')
        case 'WATER':
            return aleatorio(PokemonAgua,'WATER')
        case 'FLYING':
            return aleatorio(PokemonVoador,'FLYING')
        case 'ROCK':
            return aleatorio(PokemonPedra,'ROCK')
        case 'ELECTRIC':
            return aleatorio(PokemonEletrico,'ELECTRIC')
        case 'GROUND':
            return aleatorio(PokemonTerrestre,'GROUND')
        case 'POISON':
            return aleatorio(PokemonVenenoso,'POISON')
        case 'BUG':
            return aleatorio(PokemonInseto,'BUG')
        case 'NORMAL':
            return aleatorio(PokemonNormal,'NORMAL')
