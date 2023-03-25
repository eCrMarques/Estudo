# Utilize o conceito de herança para criar a
# Classe Pokemon e as subclasses de tipo
# de Pokemon

# ex: PokemonAquatico, PokemonFogo,
# PokemonEletrico
from Tipos import *

class Pokemon:
    def __init__(self, nome, tipo, vida, atk):
        self._nome = nome
        self._tipo = tipo
        self._vida = vida
        self._atk = atk

    def vantagem(self,Vantagem,tipoVantagem,tipoDesvantagem):
        return f'{tipoVantagem} tem {Vantagem} Contra {tipoDesvantagem}'
    

class PokemonAquatico(Pokemon):
    def __init__(self, nome, tipo, vida, atk):
        super().__init__(nome, tipo, vida, atk)
    
    def vantagem(self,inimigo):
        if inimigo._tipo=='Planta':
            return super().vantagem('Desvantagem',self._tipo,'Planta')
        elif inimigo._tipo=='Fogo':
            return super().vantagem('Vantagem',self._tipo,'Fogo')
    
class PokemonFogo(Pokemon):
    def __init__(self, nome, tipo, vida, atk):
        super().__init__(nome, tipo, vida, atk)

    def vantagem(self,inimigo):
        if inimigo._tipo=='Planta':
            return super().vantagem('Vantagem',self._tipo,'Planta')
        elif inimigo._tipo=='Agua':
            return super().vantagem('Desvantagem',self._tipo,'Agua')
        
class PokemonPlanta(Pokemon):
    def __init__(self, nome, tipo, vida, atk):
        super().__init__(nome, tipo, vida, atk)

    def vantagem(self,inimigo):
        if inimigo._tipo=='Agua':
            return super().vantagem('Vantagem',self._tipo,'Agua')
        elif inimigo._tipo=='Fogo':
            return super().vantagem('Desvantagem',self._tipo,'Fogo')

pokemon1 =PokemonAquatico("Squirtle",'Agua',165,156)
pokemon2 =PokemonFogo('Charmadner','Fogo',455,564)
pokemon3 =PokemonFogo('Bulbasaur','Planta',455,564)
print(pokemon2.vantagem(pokemon1))