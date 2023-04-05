class Locais:
    def __init__(self, rotas, npc=None, selvagens=None ,mark=None, centro=None ):
        self.npc=npc
        self.mark=mark
        self.centro=centro
        self.selvagens=selvagens
        self.rotas=rotas
    
    def centro(self):
        pass

    def mark(self):
        pass

Pallet=Locais('Caminho de Viridian',selvagens=['Pidgey','Rattata','Caterpie'])
Viridian=Locais(('Liga Pokemon','Viridian Florest'))
print(Viridian.rotas[0])
#Planta , Inseto, Venenoso, 
class Floresta(Locais):
    def __init__(self, npc):
        super().__init__(npc)
        selvagens=['Oddish', 'Paras', 'Bellsprout','Exeggcute','Caterpie','Metapod','Weedle','Kakuna','Venonat',]
floresta=Floresta('Josh')

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

