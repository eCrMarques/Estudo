# Sua vez

# Crie uma classe chamada Pokemon. Tente imaginar os
# atributos que um objeto dessa classe teria.
# Faça um programa que instância um objeto da classe
# Pokemon e imprima os atributos desse objeto.
# Bônus: Crie 2 objetos Pokemon e tente criar uma função
# de batalha que recebe os 2 objetos e determine quem sai
# ganhando.
import random
class Pokemon:
    def __init__(self,nome,tipo,ataque,vida,velocidade,apelido=None):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.vida = vida
        self.velocidade = velocidade
        #Apelido
        if apelido!=None:
            self.nome=apelido

    #Pokemon Selvagem Aleatorio
    def Selvagem():
        dex={'Rattata':{
            'tipo':'Normal',
            'ataque':56,
            'vida':30,
            'velocidade':72,
        },'Pidgey':{
            'tipo':'Voador',
            'ataque':45,
            'vida':40,
            'velocidade':56,},
        'Weedle':{
            'tipo':'Inseto',
            'ataque':35,
            'vida':40,
            'velocidade':50,},
        'Caterpie':{
            'tipo':'Inseto',
            'ataque':30,
            'vida':45,
            'velocidade':45,},
        'Metapod':{
            'tipo':'Inseto',
            'ataque':20,
            'vida':50,
            'velocidade':30,},
        'Kakuna':{
            'tipo':'Inseto',
            'ataque':25,
            'vida':45,
            'velocidade':35,}}
        poke=random.choice(['Rattata','Pidgey','Weedle','Caterpie','Metapod','Kakuna'])
        Selvagem = Pokemon(poke,dex[poke]['tipo'],dex[poke]['ataque'],dex[poke]['vida'],dex[poke]['velocidade'])
        return Selvagem


    #Pokemon Mais Veloz
    def speed(pokemon1,pokemon2):
        lista=[]
        if pokemon1>pokemon2:
            return pokemon1
        else:
            return pokemon2

    def atacar(self,oponente):
        contador=0
        # Inverter os Pokemons caso a velocidade do inimigo seja maior
        if self.velocidade != Pokemon.speed(self.velocidade,oponente.velocidade):
            copia =self.__dict__.copy
            self.__dict__=oponente.__dict__
            oponente.__dict__=copia()
            contador=10


        #Batalha Pokemon
        while True:
            if self.velocidade>= oponente.velocidade:
                oponente.vida = oponente.vida - int(self.ataque/10)
                if oponente.vida<=0:
                    print(f'///////////\n//{self.nome}//\n///////////\n----WIN----')
                    break
                else:
                    print(f'{self.nome} Atacou: {oponente.nome}\nVida Restante: // {oponente.vida} //\n')
                    self.vida = self.vida - int(oponente.ataque/10)
                    if self.vida<=0:
                        print(f'///////////\n//{oponente.nome}//\n///////////\n----WIN----')
                        break
                    else:
                        print(f'{oponente.nome} Atacou: {self.nome}\nVida Restante: // {self.vida} //\n')


        #Corrigir a inversão caso os Pokemons Tenham sido Invertido
        if contador==10:
            copia =self.__dict__.copy
            self.__dict__=oponente.__dict__
            oponente.__dict__=copia()
def Menu():
    print('---------------MENU---------------\n      1 --- Lutar ---- 1\n      2 --- Curar --- 2\n      3 --- Explorar --- 3')
    return int(input('\n--- Escolha: '))


meuPokemon= Pokemon('Charmander','Fogo',52,39,65,'Char')
pokemon1 = Pokemon('Charmander','Fogo',52,39,65)
pokemon2= Pokemon('Rattata','Normal',56,30,72)
pokemon3= Pokemon('Fearow','Voador',90,65,100)

#Atacar
print(pokemon1.__dict__)
print(Pokemon.Selvagem().__dict__)

#Explorar
if Menu() ==3 :
    print(meuPokemon.atacar(Pokemon.Selvagem()))




'''    def atacar(self,time,oponente):
        while True:
            if self.velocidade>= oponente.velocidade and self.vida>0 and oponente.vida>0: 
                self.vida = oponente.vida - int(self.ataque/10)
                if self.vida<=0:
                    print(f'///////////\n//{oponente.nome}//\n///////////\n----WIN----')
                    break
                else:
                    print(f'{oponente.nome} Atacou: {self.nome}\nVida Restante: // {self.vida} //\n')
                    oponente.vida = self.vida - int(oponente.ataque/10)
                    if oponente.vida<=0:
                        print(f'///////////\n//{self.nome}//\n///////////\n----WIN----')
                        break
                    else:
                        print(f'{self.nome} Atacou: {oponente.nome}\nVida Restante: // {oponente.vida} //\n')
            elif oponente.velocidade>= self.velocidade and oponente.vida>0 and self.vida>0: 
                oponente.vida = self.vida - int(oponente.ataque/10)
                if oponente.vida<=0:
                    print(f'///////////\n//{self.nome}//\n///////////\n----WIN----')
                    break
                else:
                    print(f'{self.nome} Atacou: {oponente.nome}\nVida Restante: // {oponente.vida} //\n')
                    self.vida = oponente.vida - int(self.ataque/10)
                    if self.vida<=0:
                        print(f'///////////\n//{oponente.nome}//\n///////////\n----WIN----')
                        break
                    else:
                        print(f'{oponente.nome} Atacou: {self.nome}\nVida Restante: // {self.vida} //\n')'''