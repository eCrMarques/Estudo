from Pokemon import *
from Textos import *
import random


class Treinador:
    def __init__(self, nome, pokemons=None, dinheiro=None):
        self.nome=nome
        if dinheiro==None:
            self.dinheiro=500
        else:
            self.dinheiro=dinheiro
        if pokemons==None:
            self.pokemons=[]
        elif type(pokemons)==list:
            self.pokemons=pokemons
        else:
            self.pokemons=pokemons

    def time(self):
        lista =[]
        for i in self.pokemons:
            lista.append(i.nome)
        return lista

    def capturar(self,pokemon):
        if type(pokemon) ==str :
            pokemon=NomePokemon(pokemon)
        self.pokemons.append(pokemon)

    def batalha(self,oponente,indextime=None ,indexinimigo=None,):
        resultado=True
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
            continuar= True
            for pokemon in self.pokemons:
                if pokemon.hp>0:
                    continuar= False
            if continuar:
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

                escolha=self.OpçõesLuta(self.bag[0])
                if escolha:
                    if escolha =='Capturado':
                        print(oponente.nome, 'Capturado')
                        self.capturar(oponente)
                        self.bag.append('')
                        self.bag.pop(0)
                        pokemoninimigo.hp=0
                    else:
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

                escolha=self.OpçõesLuta(self.bag[0])
                if escolha:
                    if escolha =='Capturado':
                        print(oponente.nome, 'Capturado')
                        self.capturar(oponente)
                        pokemoninimigo.hp=0
                        self.bag.append('')
                        self.bag.pop(0)
                    else:
                        print(f'Seu {self.pokemons[poketime].nome} Ataca o {pokemoninimigo.nome} com {timeAtaque} de Dano')
                        pokemoninimigo.hp-=timeAtaque

        oponenteDinheiro=random.randrange(300,750)
        if pokemoninimigo.hp<=0:
            if (len(oponente.pokemons)-1)>pokeinimigo:
                pokeinimigo=pokeinimigo+1
                self.batalha(oponente,poketime,pokeinimigo)
            else:
                print(f'\t    {self.nome}\n'
                      '------=========WIN=========------')
                resultado=True
                if oponente.__class__==Oponente:
                    self.dinheiro+=oponenteDinheiro
                    print(f"Você Ganhou {oponenteDinheiro} de Dinheiro")
                    
        elif self.pokemons[poketime].hp<=0:
            self.pokemons[poketime].hp=0
            if (len(self.pokemons)-1)>poketime:
                    poketime=poketime+1
                    self.batalha(oponente,poketime,pokeinimigo)
            else:
                print(f'\t    {oponente.nome}\n'
                      '------=========WIN=========------')
                resultado=False
                if oponente.__class__==Oponente:
                    self.dinheiro-=oponenteDinheiro
                    print(f"Você Perdeu {oponenteDinheiro} de Dinheiro")
                    
        return resultado        

            

class Jogador(Treinador):
    def __init__(self, nome, pokemons=None, dinheiro=None):
        super().__init__(nome, pokemons, dinheiro)
        self.bag=['']
    def batalha(self, oponente, indextime=None, indexinimigo=None):
        return super().batalha(oponente, indextime, indexinimigo,)
    
    def Mochila(self,item):
            if '' in self.bag:
                self.bag.remove('')
            self.bag.append(item)
            print(self.bag)

    def VerMochila(self):
        print('\tSeus Pokemons são\n')
        pokemons=''
        for pokemon in self.pokemons:
            pokemons=pokemons+' -//- '+str(pokemon.nome)+'('+str(pokemon.hp)+')'
        print(pokemons)
        if len(self.bag)!=0:
            items=''
            print('\t-Items-')
            for item in (set(self.bag)):
                if item!='':
                    items=items+str(item)+': '+ str(self.bag.count(item))+' // '
            print(items)
            input()

    def OpçõesLuta(self,item=None):
        lprint(f'1 -- Atacar\n'
                    '2 -- Mochila\n'
                    '3 -- Capturar\n')
        num=input()
        match num:
            case '1':
                return True
            case '2':
                self.VerMochila()
            case '3':
                if Capturar(item):
                    return 'Capturado'
                else:
                    print('Falhou em capturar')
                    print(item)
            case _:
                print('Opção Inexistente')

    


class Oponente(Treinador):
    def __init__(self, nome, pokemons, dinheiro):
        super().__init__(nome, pokemons, dinheiro)