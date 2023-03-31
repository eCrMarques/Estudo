from Textos import *
from Pokemon import *
from Treinadores import *
from locais import *
import random 
cidade='Pallet'
def listaLocais(locais):
     n=0
     if type(locais)==str:
         print(f'{1}--{locais}')
     else:
          for i in locais:
               n+=1
               print(f'{n}--{i}')
     

def Explorar(cidade):
    print(f'''\t\t---Local atual: {cidade}--- ''')
    n=0
    match cidade:
        case "Pallet":
            listaLocais(Pallet.rotas)
            
            op=input()
            if op=='1':
               selvagem=NomePokemon(Pallet.selvagens)
               opçõesCidade('Viridian')
        case 'Viridian':
            listaLocais(Viridian.rotas)

def opçõesCidade(Nome=None):

    if Nome==None:
        Nome=cidade
    else:
        Nome=Nome
    print(f'''
        \t---Local atual: {Nome}--- \n
        1-- Explorar
        2-- Procurar Treinadores
        3-- Centro Pokemon
        4-- Market''')
    match input(''):
        case '1':
            Explorar(Nome)
        case '2':
            Treinadores()
        case '3':
            Textos('Centro')
        case '4':
            Textos('Mark')


if Menu(0.05):
    print('''
    Seja Bem-Vindo a sua aventura pokemon, primeiro precisamos saber o seu Nome''')
    Nome=input('')
    Player=Jogador(Nome,dinheiro=500)
    print(f'''\nBom {Nome} Para Começar Sua Aventura Escolha o seu primeiro Pokemon
    1-- Charmander
    2-- Squirtle
    3-- Bulbasaur\n''')

    op =input('')
    match op:
        case '1':
            Player.capturar('Charmander')
        case '2':
            Player.capturar('Squirtle')
        case '3':
            Player.capturar('Bulbasaur')

    opçõesCidade()
        
    
