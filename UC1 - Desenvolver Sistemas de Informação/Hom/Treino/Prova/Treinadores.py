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
        if type(pokemon) ==str :
            pokemon=NomePokemon(pokemon)
        self.pokemons.append(pokemon)
        with open ('Save.txt','w') as arquivo:
            for pokemon in self.pokemons:
                arquivo.write(f'{pokemon.nome},{pokemon.tipo},{pokemon.hp},{pokemon.atk},{pokemon.df},{pokemon.spd}\n')
        return f'Pokemon Capturado: {pokemon}'

    def batalha(self,oponente,indextime=None ,indexinimigo=None,):
        resultado=False
        if indextime ==None:
            poketime=0

        else:
            poketime=indextime

        if indexinimigo== None:
            pokeinimigo=0

        else:
            pokeinimigo=indexinimigo

        if oponente.__class__ == Oponente:
            pokemoninimigo=oponente.pokemons[pokeinimigo]
            Time=f'Time inimigo : {oponente.time()}'
            Nome = oponente.nome

        else:
            pokemoninimigo=oponente
            Time= ''
            Nome =''
            oponente.pokemons=[pokemoninimigo]

        if self.pokemons[poketime].hp<=0:
            return

        while True:
            timeAtaque=self.pokemons[poketime].checarDano(pokemoninimigo)
            oponenteAtaque=pokemoninimigo.checarDano(self.pokemons[poketime])


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
                self.batalha(oponente,poketime,pokeinimigo)
            else:
                print(f'\t    {self.nome}\n'
                      '------=========WIN=========------')
                resultado=True
                if oponente.__class__==Oponente:
                    print("Você Ganhou YYYYY de Dinheiro")
                    
        elif self.pokemons[poketime].hp<=0:
            if (len(self.pokemons)-1)>poketime:
                    poketime=poketime+1
                    Player.batalha(oponente,poketime,pokeinimigo)
            else:
                print(f'\t    {oponente.nome}\n'
                      '------=========WIN=========------')
                'Perdeu'
                resultado=False
                if oponente.__class__==Oponente:
                    print("Você Perdeu YYYYY de Dinheiro")
                    
        return resultado        

            

class Jogador(Treinador):
    def __init__(self, nome, pokemons=None, dinheiro=None):
        super().__init__(nome, pokemons, dinheiro)

    def batalha(self, oponente, indextime=None, indexinimigo=None):
        return super().batalha(oponente, indextime, indexinimigo)
    
class Oponente(Treinador):
    def __init__(self, nome, pokemons, dinheiro):
        super().__init__(nome, pokemons, dinheiro)
    


