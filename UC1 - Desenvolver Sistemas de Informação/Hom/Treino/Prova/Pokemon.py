import random
from Dex import *

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
        dano=self.checarVantagem(oponente)*(((self.atk/oponente.df)+2)*1.5)*random.uniform(1.5,3.0)
        return int(dano)
    
class Fogo(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Fogo'
        self.movimentos=[]
        self.vantagem=['Aço', 'Gelo','Inseto','Planta',]
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
        self.desvantagem=['Elétrico' ,'Gelo' , 'Pedra']

class Pedra(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Pedra'
        self.movimentos=[]
        self.vantagem=['Fogo', 'Gelo', 'Inseto' , 'Voador ']
        self.desvantagem=['Aço', 'Água', 'Lutador', 'Planta' , 'Terrestre']
    
class Inseto(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Inseto'
        self.movimentos=[]
        self.vantagem=['Planta' , 'Psíquico']
        self.desvantagem=['Fogo','Voador ','Pedra']

class Normal(Pokemon):
    def __init__(self, nome, tipo ,hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Normal'
        self.movimentos=[]
        self.vantagem=['']
        self.desvantagem=['Lutador']

class Terrestre(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Terrestre'
        self.movimentos=[]
        self.vantagem=['Aço', 'Elétrico', 'Fogo', 'Pedra' , 'Venenoso']
        self.desvantagem=['Água', 'Gelo' , 'Planta']

class Venenoso(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo='Venenoso'
        self.movimentos=[]
        self.vantagem=['Fada' , 'Planta']
        self.desvantagem=['Psíquico' , 'Terrestre']

class Aço(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo=''
        self.movimentos=[]
        self.vantagem=['Fada','Gelo','Pedra']
        self.desvantagem=['Fogo', 'Lutador' ,'Terrestre']
class Dragao(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo=''
        self.movimentos=[]
        self.vantagem=[]
        self.desvantagem=['Dragão', 'Fada' , 'Gelo']
class Fada(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo=''
        self.movimentos=[]
        self.vantagem=['Dragão', 'Lutador' ]
        self.desvantagem=['Lutador', 'Inseto']
class Fantasma(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo=''
        self.movimentos=[]
        self.vantagem=['Fantasma' ]
        self.desvantagem=['Inseto' , 'Psíquico']
class Gelo(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo=''
        self.movimentos=[]
        self.vantagem=['Dragão', 'Planta', 'Terrestre' , 'Voador']
        self.desvantagem=['Aço', 'Fogo', 'Lutador' , 'Pedra']
class Lutador(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo=''
        self.movimentos=[]
        self.vantagem=['Aço', 'Gelo', 'Normal', 'Pedra' ]
        self.desvantagem=['Fada', 'Psíquico' , 'Voador']
class Psiquico(Pokemon):
    def __init__(self, nome, tipo, hp, atk, df, spd):
        super().__init__(nome, tipo, hp, atk, df, spd)
        self.tipo=''
        self.movimentos=[]
        self.vantagem=['Lutador' , 'Venenoso']
        self.desvantagem=['Fantasma', 'Inseto' ]

class Locais:
    def __init__(self, npc, selvagens ,mark=None, centro=None ):
        self.npc=npc
        self.mark=mark
        self.centro=centro
        self.selvagens=selvagens
    
    def centro(self):
        pass

    def mark(self):
        pass

#Planta , Inseto, Venenoso, 
class Floresta(Locais):
    def __init__(self, npc, selvagens):
        super().__init__(npc)
        selvagens=['Oddish', 'Paras', 'Bellsprout','Exeggcute','Caterpie','Metapod','Weedle','Kakuna','Venonat',]
    
#Terrestre , Pedra, 
class CavernaDiglett(Locais):
    def __init__(self, npc, selvagens):
        super().__init__(npc)
        selvagens=['Sandshrew','Diglett','Cubone','Zubat',]
    
# Terrestre+ , Pedra+, Steel+, Lutador, Fada
class MountainMoon(Locais):
    def __init__(self, npc, selvagens):
        super().__init__(npc)
        selvagens=['Dugtrio','Geodude', 'Graveler', 'Onix','Cubone','Rhyhorn','Machop','Machoke','Clefairy','Jigglypuff','Wigglytuff']
    
#Voador Venenoso, Psyquico, Terrestre+, Pedra+
class CeruleanCave(Locais):
    def __init__(self, npc, selvagens):
        super().__init__(npc)
        selvagens=['Dugtrio', 'Marowak','Sandshrew', 'Zubat' 'Golbat','Slowpoke','Abra', 'Drowzee']
    
#Pedra++ , Steel++, Lutador++
class RockTunnel(Locais):
    def __init__(self, npc, selvagens):
        super().__init__(npc)
        selvagens=['Graveler', 'Golem','Rhydon','Machamp', 'Machoke', 'Parasect' ]
    
#Eletrico, Planta
class PowerPlant(Locais):
    def __init__(self, npc, selvagens):
        super().__init__(npc)
        selvagens=['Gloom','Weepinbell', 'Nidorina', 'NidoranF', 'NidoranM', 'Nidorino','Bulbasaur','Pikachu','Magnemite','Voltorb',]
    
#Fantasma
class PokemonTower(Locais):
    def __init__(self, npc, selvagens):
        super().__init__(npc)
        selvagens=['Gastly', 'Haunter', 'Gengar', 'Marowak', 'Raticate',]
    
#Normal, Lutador, Aquatico, Inseto, Fada
class Safari(Locais):
    def __init__(self, npc, selvagens):
        super().__init__(npc)
        selvagens=['Mr. Mime', 'Clefable', 'Nidoking', 'Nidoqueen','Dratini', 'Mr. Mime', 'Exeggutor', 'Slowbro', 'Kadabra', 'Hypno', 'Butterfree', 'Eevee', 'Tauros','Kangaskhan', 'Lickitung', 'Dodrio']
    
#Fogo+- ,Venenoso++, Fantasma+
class CinnabarMansion(Locais):
    def __init__(self, npc, selvagens):
        super().__init__(npc)
        selvagens=['Vulpix', 'Ninetales', 'Growlithe', 'Arcanine', 'Ponyta', 'Rapidash', 'Magmar', 'Flareon','Charmander','Grimer', 'Muk', 'Koffing', 'Weezing', 'Ekans', 'Arbok']


def aleatorio(classe,tipo):
    try:
        aleatorio=random.choice(pokemonstipo(tipo))
        local =Pokedex.index(aleatorio)
        return classe(Pokedex[local],'',Pokedex[local+1]['Hp'],Pokedex[local+1]['Atk'],Pokedex[local+1]['Def'],Pokedex[local+1]['Speed'])
    except:
        aleatorio=tipo
        print(aleatorio)
        local =Pokedex.index(aleatorio)
        return classe(Pokedex[local],'',Pokedex[local+1]['Hp'],Pokedex[local+1]['Atk'],Pokedex[local+1]['Def'],Pokedex[local+1]['Speed'])

def Selvagem(tipo):
    match tipo:
        case 'Planta':
            return aleatorio(Planta,'Planta')
        case 'Fogo':
            return aleatorio(Fogo,'Fogo')
        case 'Agua':
            return aleatorio(Agua,'Agua')
        case 'Voador':
            return aleatorio(Voador,'Voador')
        case 'Pedra':
            return aleatorio(Pedra,'Pedra')
        case 'Eletrico':
            return aleatorio(Eletrico,'Eletrico')
        case 'Terrestre':
            return aleatorio(Terrestre,'Terrestre')
        case 'Venenoso':
            return aleatorio(Venenoso,'Venenoso')
        case 'Inseto':
            return aleatorio(Inseto,'Inseto')
        case 'Normal':
            return aleatorio(Normal,'Normal')
        case 'Aço':
            return aleatorio(Aço,'Aço')
        case 'Dragao':
            return aleatorio(Dragao,'Dragao')
        case 'Fada':
            return aleatorio(Fada,'Fada')
        case 'Fantasma':
            return aleatorio(Fantasma,'Fantasma')
        case 'Gelo':
            return aleatorio(Gelo,'Gelo')
        case 'Lutador':
            return aleatorio(Lutador,'Lutador')
        case 'Psiquico':
            return aleatorio(Psiquico,'Psiquico')
        case 'Normal':
            return aleatorio(Normal,'Normal')

from locais import *

def NomePokemon(pokemon):
    if type(pokemon) == str:
        Selvagem=pokemon
    elif type(pokemon) == list:
        Selvagem=random.choice(pokemon)
    local =Pokedex.index(Selvagem)
    tipo=Pokedex[local+1]['tipo']
    if len(tipo)<=2:
        tipo=tipo[0]

    match tipo:
        case 'Planta':
            return aleatorio(Planta,Selvagem)
        case 'Fogo':
            return aleatorio(Fogo,Selvagem)
        case 'Agua':
            return aleatorio(Agua,Selvagem)
        case 'Voador':
            return aleatorio(Voador,Selvagem)
        case 'Pedra':
            return aleatorio(Pedra,Selvagem)
        case 'Eletrico':
            return aleatorio(Eletrico,Selvagem)
        case 'Terrestre':
            return aleatorio(Terrestre,Selvagem)
        case 'Venenoso':
            return aleatorio(Venenoso,Selvagem)
        case 'Inseto':
            return aleatorio(Inseto,Selvagem)
        case 'Normal':
            return aleatorio(Normal,Selvagem)
        case 'Aço':
            return aleatorio(Aço,Selvagem)
        case 'Dragao':
            return aleatorio(Dragao,Selvagem)
        case 'Fada':
            return aleatorio(Fada,Selvagem)
        case 'Fantasma':
            return aleatorio(Fantasma,Selvagem)
        case 'Gelo':
            return aleatorio(Gelo,Selvagem)
        case 'Lutador':
            return aleatorio(Lutador,Selvagem)
        case 'Psiquico':
            return aleatorio(Psiquico,Selvagem)
        case 'Normal':
            return aleatorio(Normal,Selvagem)




#     match tipo:
#         case 'Planta':
#             return aleatorio(Planta,'Planta')
#         case 'Fogo':
#             return aleatorio(Fogo,'Fogo')
#         case 'Agua':
#             return aleatorio(Agua,'Agua')
#         case 'Voador':
#             return aleatorio(Voador,'Voador')
#         case 'Pedra':
#             return aleatorio(Pedra,'Pedra')
#         case 'Eletrico':
#             return aleatorio(Eletrico,'Eletrico')
#         case 'Terrestre':
#             return aleatorio(Terrestre,'Terrestre')
#         case 'Venenoso':
#             return aleatorio(Venenoso,'Venenoso')
#         case 'Inseto':
#             return aleatorio(Inseto,'Inseto')
#         case 'Normal':
#             return aleatorio(Normal,'Normal')
#         case 'Aço':
#             return aleatorio(Aço,'Aço')
#         case 'Dragao':
#             return aleatorio(Dragao,'Dragao')
#         case 'Fada':
#             return aleatorio(Fada,'Fada')
#         case 'Fantasma':
#             return aleatorio(Fantasma,'Fantasma')
#         case 'Gelo':
#             return aleatorio(Gelo,'Gelo')
#         case 'Lutador':
#             return aleatorio(Lutador,'Lutador')
#         case 'Psiquico':
#             return aleatorio(Psiquico,'Psiquico')
#         case 'Normal':
#             return aleatorio(Normal,'Normal')
# print(aleatorio(Planta,'Venusaur'))