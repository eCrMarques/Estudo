import random
from Dex import *

def aleatorio(classe,tipo):
    aleatorio=random.choice(pokemonstipo(tipo))
    local =Pokedex.index(aleatorio)
    return classe(Pokedex[local],'',Pokedex[local+1]['Hp'],Pokedex[local+1]['Atk'],Pokedex[local+1]['Def'],Pokedex[local+1]['Speed'])


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
    
    def checarVantagem(self, oponente):
        if oponente.tipo in self.vantagem:
            return 2
        elif oponente.tipo in self.desvantagem:
            return 0.5
        else:
            return 1
        
    def checarDano(self,oponente):
        dano=self.checarVantagem(oponente)*self.atk/10
        return int(dano)
    
class Fogo(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Fogo'
        self.movimentos=[]
        self.vantagem=['Inseto','Planta',]
        self.desvantagem=['Pedra','Terrestre','Agua']

class Agua(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Agua'
        self.movimentos=[]
        self.vantagem=['Fogo','Terrestre','Pedra']
        self.desvantagem=['Elétrico ','Planta']

class Planta(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Planta'
        self.movimentos=[]
        self.vantagem=['Terrestre','Pedra ','Água']
        self.desvantagem=['Inseto','Fogo','Voador']

class Eletrico(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Eletrico'
        self.movimentos=[]
        self.vantagem=['Água ','Voador']
        self.desvantagem=['Terrestre']

class Voador(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Voador'
        self.movimentos=[]
        self.vantagem=['Inseto','Lutador','Planta']
        self.desvantagem=['Elétrico','Pedra']

class Pedra(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Pedra'
        self.movimentos=[]
        self.vantagem=['Inseto','Fogo ','Voador ']
        self.desvantagem=['Planta','Terrestre','Água']
    
class Inseto(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Inseto'
        self.movimentos=[]
        self.vantagem=['Planta ',]
        self.desvantagem=['Fogo','Voador ','Pedra']

class Normal(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Normal'
        self.movimentos=[]
        self.vantagem=['Lutador']
        self.desvantagem=['Fantasma']

class Terrestre(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Terrestre'
        self.movimentos=[]
        self.vantagem=[]
        self.desvantagem=[]

class Venenoso(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Venenoso'
        self.movimentos=[]
        self.vantagem=[]
        self.desvantagem=[]


def Selvagem(tipo):
    match tipo:
        case 'GRASS':
            return aleatorio(Planta,'GRASS')
        case 'FIRE':
            return aleatorio(Fogo,'FIRE')
        case 'WATER':
            return aleatorio(Agua,'WATER')
        case 'FLYING':
            return aleatorio(Voador,'FLYING')
        case 'ROCK':
            return aleatorio(Pedra,'ROCK')
        case 'ELECTRIC':
            return aleatorio(Eletrico,'ELECTRIC')
        case 'GROUND':
            return aleatorio(Terrestre,'GROUND')
        case 'POISON':
            return aleatorio(Venenoso,'POISON')
        case 'BUG':
            return aleatorio(Inseto,'BUG')
        case 'NORMAL':
            return aleatorio(Normal,'NORMAL')

def EscolherPokemon(Nome):
    local =Pokedex.index(Nome)+1
    if len(Pokedex[local]['tipo'])>1:
        classe=Pokedex[local]['tipo'][0]
        print(classe)
    else:
        classe=Pokedex[local]['tipo']
        print(classe)
EscolherPokemon('Venusaur')

# pokemon1= aleatorio(PokemonAgua,'WATER')
# pokemon2= aleatorio(PokemonFogo,'FIRE')