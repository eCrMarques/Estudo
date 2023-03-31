from Pokemon import *
from Textos import *

class Treinador:
    def __init__(self, nome, pokemons=None, dinheiro=None):
        self.nome=nome
        self.pokemons=[pokemons]
        if dinheiro==None:
            self.dinheiro=500
        else:
            self.dinheiro=dinheiro
        if pokemons==None:
            self.pokemons=[]
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
            # oponente
        if oponente.__class__ == Oponente:
            pokemoninimigo=oponente.pokemons[pokeinimigo]
            Time=f'Time inimigo : {oponente.time()}'
            Nome = oponente.nome
            grupo=oponente.pokemons

        else:
            pokemoninimigo=oponente
            Time= ''
            Nome =''
            oponente.pokemons=[pokemoninimigo]
            
        timeAtaque=self.pokemons[poketime].checarDano(pokemoninimigo)
        oponenteAtaque=pokemoninimigo.checarDano(self.pokemons[poketime])
 

        while True:
            print(f'Meu time : {self.time()} \t{Time}')
            print(f'{self.nome}\t\t\t\t\t\t {Nome}\n'
            f'{self.pokemons[poketime].nome} Vida [-------{self.pokemons[poketime].hp}-------]\t\t{pokemoninimigo.nome} Vida [-------{pokemoninimigo.hp}-------]\n')

            if self.pokemons[poketime].spd>pokemoninimigo.spd and pokemoninimigo.hp>=timeAtaque:
                
                if pokemoninimigo.hp<=0:
                    break
                elif self.pokemons[poketime].hp<=0:
                    break
                print(f'Seu {self.pokemons[poketime].nome} Esta Pronto Para a Batalha')

                if OpçõesLuta():
                    print(f'{self.nome}\t\t\t\t\t\t {oponente.nome}\n'
                f'{self.pokemons[poketime].nome} Vida [-------{self.pokemons[poketime].hp}-------]\t\t{pokemoninimigo.nome} Vida [-------{pokemoninimigo.hp}-------]\n')
                    print(f'Seu {self.pokemons[poketime].nome} Ataca o {pokemoninimigo.nome} com {timeAtaque} de Dano')
                    pokemoninimigo.hp-=timeAtaque

                    print(f'{pokemoninimigo.nome} Ataca seu {self.pokemons[poketime].nome} com {oponenteAtaque} de Dano\n')
                    self.pokemons[poketime].hp-=oponenteAtaque                    

            else:          
                
                print(f'{pokemoninimigo.nome} Ataca seu {self.pokemons[poketime].nome} com {oponenteAtaque} de Dano\n')
                self.pokemons[poketime].hp-=oponenteAtaque 

                print(f'{self.nome}\t\t\t\t\t\t {oponente.nome}\n'
                f'{self.pokemons[poketime].nome} Vida [-------{self.pokemons[poketime].hp}-------]\t\t{pokemoninimigo.nome} Vida [-------{pokemoninimigo.hp}-------]\n')
                
                if pokemoninimigo.hp<=0:
                    break
                elif self.pokemons[poketime].hp<=0:
                    break
                print(f'Seu {self.pokemons[poketime].nome} Esta Pronto Para a Batalha')
                if OpçõesLuta():
                    print(f'Seu {self.pokemons[poketime].nome} Ataca o {pokemoninimigo.nome} com {timeAtaque} de Dano')
                    pokemoninimigo.hp-=timeAtaque


        if pokemoninimigo.hp<=0:
            if (len(oponente.pokemons)-1)>pokeinimigo:
                pokeinimigo=pokeinimigo+1
                eu.batalha(oponente,poketime,pokeinimigo)
            else:
                print(f'\t    {self.nome}\n'
                      '------=========WIN=========------')
                if oponente.__class__==Oponente:
                    print("Você Ganhou YYYYY de Dinheiro")
                
        elif self.pokemons[poketime].hp<=0:
            if (len(self.pokemons)-1)>poketime:
                    poketime=poketime+1
                    eu.batalha(oponente,poketime,pokeinimigo)
            else:
                print(f'\t    {oponente.nome}\n'
                      '------=========WIN=========------')
                if oponente.__class__==Oponente:

                    print("Você Perdeu YYYYY de Dinheiro")
        

            

class Jogador(Treinador):
    def __init__(self, nome, pokemons=None, dinheiro=None):
        super().__init__(nome, pokemons, dinheiro)

    def batalha(self, oponente, indextime=None, indexinimigo=None):
        return super().batalha(oponente, indextime, indexinimigo)
    
class Oponente(Treinador):
    def __init__(self, nome, pokemons, dinheiro):
        super().__init__(nome, pokemons, dinheiro)
    

eu=Jogador('Red','Charmander',dinheiro=654)
npc=Oponente('Blue',Selvagem('GRASS'),1564)
pokemonfogo=Selvagem('FIRE')
pokemonplanta=Selvagem('GRASS')
pokemonagua= Selvagem('WATER')

print(eu.pokemons)