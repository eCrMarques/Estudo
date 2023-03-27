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

    def batalha(self,oponente , prevPokeTime, prevPokeInimigo, prevTime, posição=None):
        poketime=prevPokeTime
        pokeinimigo=prevPokeInimigo
        time=prevTime
        if posição!=None:
            match posição:
                case 'time':
                    poketime+=1
                case 'inimigo':
                    pokeinimigo+=1
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
        

        while True:
            if primeiro.hp<=0:
                if time==1:
                    if len(oponente.time())>1:
                        eu.batalha(npc,'time')
                    else:
                        print(segundo.nome,'Win')
                elif time==2:
                    if len(self.time())>1:
                        eu.batalha(npc,'inimigo')
                    else:
                        print(segundo.nome,'Win')
                break
            elif segundo.hp<=0:
                if time==1:
                    if len(oponente.time())>1:
                        eu.batalha(npc,'time')
                    else:
                        print(segundo.nome,'Win')
                elif time==2:
                    if len(self.time())>1:
                        eu.batalha(npc,'inimigo')
                    else:
                        print(segundo.nome,'Win')
                break
            
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
                print(f'{segundo.nome} Ataca seu {primeiro.nome} com {oponenteAtaque} de Dano')
                primeiro.hp-=oponenteAtaque
                
                print(f'Seu {primeiro.nome} Esta Pronto Para a Batalha')
                if OpçõesLuta():
                    print(f'Seu {primeiro.nome} Ataca o {segundo.nome} com {timeAtaque} de Dano\n')
                    segundo.hp-=timeAtaque
                      

class Jogador(Treinador):
    def __init__(self, nome, pokemons, dinheiro):
        super().__init__(nome, pokemons, dinheiro)

    def batalha(self, oponente, posição=None):
        return super().batalha(oponente, posição)

class Oponente(Treinador):
    def __init__(self, nome, pokemons, dinheiro):
        super().__init__(nome, pokemons, dinheiro)
    

eu=Jogador('Red',Selvagem('WATER'),654)
npc=Oponente('Blue',Selvagem('GRASS'),1564)
pokemonfogo=Selvagem('FIRE')
pokemonplanta=Selvagem('GRASS')

print(f'time inimigo: {npc.time()}')
print(npc.capturar(pokemonfogo),)
print(f'time inimigo: {npc.time()}\n')

print(f'time inimigo: {eu.time()}')
print(eu.capturar(pokemonplanta),)
print(f'time inimigo: {eu.time()}\n')

eu.batalha(npc, 0,0,0 )

