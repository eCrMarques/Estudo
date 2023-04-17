from Pokemon import *
from Textos import *
from Dex import *
import random

def evolução(pokemon):
    condição=False
    nome=pokemon.nome
    for lista in Evoluções:
        if pokemon.nome in lista:
            if lista.index(pokemon.nome)<len(lista)-1:
                Index=lista.index(pokemon.nome)
                evoluçãoPokemon=NomePokemon(lista[Index+1])
                condição=True
    if condição:
        if pokemon._hpanterior>evoluçãoPokemon._hp and pokemon._atk>evoluçãoPokemon._atk and pokemon._df>evoluçãoPokemon._df and pokemon._spd>evoluçãoPokemon._spd:
            evoluçãoPokemon._hpanterior+=int(pokemon._hpanterior/10)
            evoluçãoPokemon._atk+=int(pokemon._atk/10)
            evoluçãoPokemon._df+=int(pokemon._df/10)
            pokemon=evoluçãoPokemon
            loop(f'{nome} Esta Evoluindo !!!',6,0.010,False)

            return pokemon
        else:
            return pokemon
    else:
        return pokemon

class Treinador:
    def __init__(self, nome, pokemons=None, dinheiro=None):
        self.nome = nome
        if dinheiro == None:
            self.dinheiro = 500
        else:
            self.dinheiro = dinheiro
        if pokemons == None:
            self.pokemons = []
        elif type(pokemons) == list:
            self.pokemons = pokemons
        else:
            self.pokemons = [pokemons]

    def time(self):
        lista = []
        for i in self.pokemons:
            lista.append(i.nome)
        return lista

    def capturar(self, pokemon):
        if len(self.pokemons)<6 or self.pokemons==[]:
            if type(pokemon) == str:
                self.pokemons.append(NomePokemon(pokemon))
            else:
                self.pokemons.append(pokemon)

    def batalha(self, oponente, indextime=None, indexinimigo=None,):
        resultado = True
        if indextime == None:
            poketime = 0

        else:
            poketime = indextime

        if indexinimigo == None:
            pokeinimigo = 0

        else:
            pokeinimigo = indexinimigo

        if oponente.__class__ == Oponente:
            pokemoninimigo = oponente.pokemons[pokeinimigo]
            Time = f'Time inimigo : {oponente.time()}'
            Nome = oponente.nome

        else:
            pokemoninimigo = oponente
            Time = ''
            Nome = ''
            oponente.pokemons = [pokemoninimigo]

        if self.pokemons[poketime]._hp <= 0:
            continuar = True
            for i,pokemon in enumerate(self.pokemons):
                if pokemon._hp > 0:
                    continuar = False
                else:
                    poketime+=1
            if continuar:
                return
        
        while True:
            timeAtaque = self.pokemons[poketime].checarDano(pokemoninimigo)

            if pokemoninimigo._hp <= 0:
                break
            elif self.pokemons[poketime]._hp <= 0:
                break

            oponenteAtaque = pokemoninimigo.checarDano(self.pokemons[poketime])
            print(f'\t\t\t\t\t{Time}')
            print(f'{self.nome}\t\t\t\t\t\t {Nome}\n'
                  f'{self.pokemons[poketime].nome} Vida [-------{self.pokemons[poketime]._hp}-------]\t\t{pokemoninimigo.nome} Vida [-------{pokemoninimigo._hp}-------]\n')
            
            if self.pokemons[poketime]._spd > pokemoninimigo._spd and pokemoninimigo._hp >= timeAtaque:

                
                print(
                    f'Seu {self.pokemons[poketime].nome} Esta Pronto Para a Batalha')
                
                escolha = self.OpçõesLuta(self.bag[0],oponente)
                if escolha:
                    if escolha == 'Capturado':
                        print(oponente.nome, 'Capturado')
                        input()
                        if len(self.pokemons)<6:
                            self.capturar(oponente)
                            self.bag.pop(0)
                            pokemoninimigo._hp = 0
                        else:
                            print('Pokemon foi ao Centro')
                            return oponente
                    elif escolha =='Falha':
                        return self.batalha(oponente)
                    elif escolha =="Fugir":
                        break
                print(
                    f'Seu {self.pokemons[poketime].nome} Ataca o {pokemoninimigo.nome} com {timeAtaque} de Dano')
                pokemoninimigo._hp -= timeAtaque
                print(
                    f'{pokemoninimigo.nome} Ataca seu {self.pokemons[poketime].nome} com {oponenteAtaque} de Dano\n')
                self.pokemons[poketime]._hp -= oponenteAtaque
                input()                

            else:
                escolha = self.OpçõesLuta(self.bag[0],oponente)
                if escolha:
                    if escolha == 'Capturado':
                        print(oponente.nome, 'Capturado')
                        input()
                        if len(self.pokemons)<6:
                            self.capturar(oponente)
                            self.bag.pop(0)
                            pokemoninimigo._hp = 0
                        else:
                            print('Pokemon foi ao Centro')
                            return oponente
                    elif escolha =='Falha':
                        return self.batalha(oponente)
                    elif escolha =="Fugir":
                        break
                print(
                    f'{pokemoninimigo.nome} Ataca seu {self.pokemons[poketime].nome} com {oponenteAtaque} de Dano')
                self.pokemons[poketime]._hp -= oponenteAtaque
                print(
                    f'Seu {self.pokemons[poketime].nome} Ataca o {pokemoninimigo.nome} com {timeAtaque} de Dano')
                pokemoninimigo._hp -= timeAtaque
                input()
                
        if pokemoninimigo._hp <= 0:
            up=int(sum([pokemoninimigo._hp,pokemoninimigo._atk,pokemoninimigo._df,pokemoninimigo._spd])/100)
            up=int(up+random.randrange(int(up/2),up))
            self.pokemons[poketime]._hpanterior+=up
            self.pokemons[poketime]._atk+=up
            self.pokemons[poketime]._df+=up
            self.pokemons[poketime]._spd+=up
            self.pokemons[poketime]=evolução(self.pokemons[poketime])
            if self.pokemons[poketime]._hp <= 0:
                self.pokemons[poketime]._hp = 0
            if (len(oponente.pokemons)-1) > pokeinimigo:
                pokeinimigo = pokeinimigo+1
                self.batalha(oponente, poketime, pokeinimigo)
            else:
                print(f'\t{self.nome:^15}\n'
                      '------=========WIN=========------')
                resultado = True
                if oponente.__class__ == Oponente:
                    oponenteDinheiro = random.randrange((int(oponente.dinheiro*0.8)), oponente.dinheiro)
                    self.dinheiro += oponenteDinheiro
                    print(f"Você Ganhou {oponenteDinheiro} de Dinheiro")

        elif self.pokemons[poketime]._hp <= 0:
            self.pokemons[poketime]._hp = 0
            if (len(self.pokemons)-1) > poketime:
                poketime = poketime+1
                self.batalha(oponente, poketime, pokeinimigo)
            else:
                print(f'\t    {oponente.nome:^15}\n'
                      '------=========WIN=========------')
                resultado = False
                if oponente.__class__ == Oponente:
                    oponenteDinheiro = random.randrange((int(oponente.dinheiro*0.8)), oponente.dinheiro)

                    if oponenteDinheiro>self.dinheiro:
                        self.dinheiro=0
                    else:
                        self.dinheiro -= oponenteDinheiro
                    print(f"Você Perdeu {oponenteDinheiro} de Dinheiro")

        return resultado


class Jogador(Treinador):
    def __init__(self, nome, pokemons=None, dinheiro=None):
        super().__init__(nome, pokemons, dinheiro)
        self.bag = ['']

    def batalha(self, oponente, indextime=None, indexinimigo=None):
        return super().batalha(oponente, indextime, indexinimigo,)

    def Mochila(self, item):
        self.bag.insert(0,item)
        

    def VerMochila(self):
        while True:
            print(f'\t{self.nome} -- Dinheiro {self.dinheiro}\n=--Seus Pokemons são--=\n')
            pokemons = ''
            for pokemon in self.pokemons:
                pokemons = pokemons+' -//- ' + \
                    str(pokemon.nome)+'('+str(pokemon._hp)+')'
            print(pokemons)
            if len(self.bag) != 0:
                items = ''
                print('\t-Items-')
                for item in (set(self.bag)):
                    if item != '':
                        items = items+str(item)+': ' + \
                            str(self.bag.count(item))+' // '
                print(items)
            if len(self.pokemons)>1:
                op=input('Trocar Pokemons - (Posição-NumPokemon)\ns-- Sair\n')
                if op.lower()=='s':
                    break
                try:
                    op=op.split('-')
                    reserva=self.pokemons[int(op[0])-1]
                    self.pokemons[int(op[0])-1]=self.pokemons[int(op[1])-1]
                    self.pokemons[int(op[1])-1]=reserva
                except:
                    print("Digite Corretamente")
            else:
                input()
                return
        
    def OpçõesLuta(self, item=None,inimigo=None):
        lprint(f'1 -- Atacar\n'
               '2 -- Mochila\n'
               '3 -- Capturar\n'
               '4 -- Fugir\n')
        num = input()
        match num:
            case '1':
                return True
            case '2':
                self.VerMochila()
                return 'Falha'
            case '3':
                if inimigo.__class__ == Oponente:
                    print("Impossivel Capturar o Pokemon do Treinador")
                    input()
                    return 'Falha'
                else:
                    if self.bag[0]=='':
                        print('Você Não Tem Pokebolas')
                        input()
                        return 'Falha'
                    else:
                        if Capturar(item):
                            return 'Capturado'
                        else:
                            print('Falhou em capturar')
                            self.bag.pop(0)
                            input()
                            return 'Falha'
            case '4':
                print("Você Fugiu!!")
                input()
                return "Fugir"
            case _:
                print('Opção Inexistente')
                return 'Falha'


class Oponente(Treinador):
    def __init__(self, nome, pokemons, dinheiro):
        super().__init__(nome, pokemons, dinheiro)
