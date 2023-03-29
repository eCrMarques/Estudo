from Pokemon import *
from Textos import *
from testes import *

class Treinador:
    def __init__(self, nome, pokemons, dinheiro):
        self.nome=nome
        self.pokemons=[pokemons]
        self.dinheiro=dinheiro
    
    def time(self):
        lista =[]
        for i in self.pokemons:
            lista.append(i.nome)
        return lista
    
    def capturar(self,pokemon):
        self.pokemons.append(pokemon)
        return f'Pokemon Capturado: {pokemon.nome}'

    def batalha(self,oponente,indextime=None ,indexinimigo=None,):
        if indextime ==None:
            poketime=0
        else:
            poketime=indextime

        if indexinimigo== None:
            pokeinimigo=0
        else:
            pokeinimigo=indexinimigo
        time=0
        if oponente.__class__ ==Oponente:
            if self.pokemons[poketime].spd>=oponente.pokemons[pokeinimigo].spd:
                primeiro=self.pokemons[poketime]
                segundo=oponente.pokemons[pokeinimigo]
                timeAtaque=primeiro.checarDano(segundo)
                oponenteAtaque=segundo.checarDano(primeiro)
            else:
                primeiro=oponente.pokemons[pokeinimigo]
                segundo=self.pokemons[poketime]
                oponenteAtaque=segundo.checarDano(primeiro)
                timeAtaque=primeiro.checarDano(segundo)
        else:
            primeiro=self.pokemons[poketime]
            segundo=oponente.pokemons[pokeinimigo]
            timeAtaque=primeiro.checarDano(segundo)
            oponenteAtaque=segundo.checarDano(primeiro)
        
        print(f'Meu time : {len(self.time())} posição: {poketime}\n'
                f'Time inimigo : {len(oponente.time())} posição: {pokeinimigo}')
        while True:

            
            print(f'{self.nome}\t\t\t\t\t\t {oponente.nome}\n'
                  f'{self.pokemons[poketime].nome} Vida [-------{primeiro.hp}-------]\t\t{oponente.pokemons[pokeinimigo].nome} Vida [-------{segundo.hp}-------]\n')
            
            if primeiro==self.pokemons[poketime] and segundo.hp>=int(primeiro.atk/10):
                print(f'Seu {primeiro.nome} Esta Pronto Para a Batalha')
                if OpçõesLuta():
                    time=1
                    print(f'Seu {primeiro.nome} Ataca o {segundo.nome} com {timeAtaque} de Dano')
                    segundo.hp-=timeAtaque

                    print(f'{segundo.nome} Ataca seu {primeiro.nome} com {oponenteAtaque} de Dano\n')
                    primeiro.hp-=oponenteAtaque
            else:
                time=2
                print(f'Seu {segundo.nome} Ataca o {primeiro.nome} com {timeAtaque} de Dano\n')
                primeiro.hp-=oponenteAtaque
                
                print(f'Seu {segundo.nome} Esta Pronto Para a Batalha')
                if OpçõesLuta():
                    print(f'{primeiro.nome} Ataca seu {segundo.nome} com {oponenteAtaque} de Dano')
                    segundo.hp-=timeAtaque
                        
            if primeiro.hp<=0:
                if primeiro.nome==oponente.pokemons[pokeinimigo].nome:
                    if (len(oponente.time())-1)>pokeinimigo:
                        pokeinimigo=pokeinimigo+1
                        eu.batalha(npc,poketime,pokeinimigo)
                    else:
                        print(segundo.nome,'Win')
                        break
                elif segundo.nome==self.pokemons[poketime].nome:
                    if (len(self.time())-1)>poketime:
                        poketime=poketime+1
                        eu.batalha(npc,poketime,pokeinimigo)
                    else:
                        print(segundo.nome,'Win')
                        break
            elif segundo.hp<=0:
                if segundo.nome==oponente.pokemons[pokeinimigo].nome:
                    if (len(oponente.time())-1)>pokeinimigo:
                        pokeinimigo=pokeinimigo+1
                        eu.batalha(npc,poketime,pokeinimigo)
                    else:
                        print(segundo.nome,'Win')
                elif segundo.nome==self.pokemons[poketime].nome:
                    if (len(self.time())-1)>poketime:
                        poketime=poketime+1
                        eu.batalha(npc,poketime,pokeinimigo)
                    else:
                        print(primeiro.nome,'Win')
                        break 

class Jogador(Treinador):
    def __init__(self, nome, pokemons, dinheiro):
        super().__init__(nome, pokemons, dinheiro)

    def batalha(self, oponente, indextime=None, indexinimigo=None):
        return super().batalha(oponente, indextime, indexinimigo)
    
class Oponente(Treinador):
    def __init__(self, nome, pokemons, dinheiro):
        super().__init__(nome, pokemons, dinheiro)
    

eu=Jogador('Red',Selvagem('WATER'),654)
npc=Oponente('Blue',Selvagem('GRASS'),1564)
pokemonfogo=Selvagem('FIRE')
pokemonplanta=Selvagem('GRASS')
pokemonagua= Selvagem('WATER')

print(f'time inimigo: {npc.time()}')
print(npc.capturar(pokemonfogo))
print(npc.capturar(pokemonagua))
print(f'time inimigo: {npc.time()}\n')

print(f'Meu time: {eu.time()}')
print(eu.capturar(pokemonplanta))
print(eu.capturar(pokemonfogo))
print(f'Meu time: {eu.time()}\n')

eu.batalha(npc)

#['Squirtle', 'Ivysaur', 'Vulpix']