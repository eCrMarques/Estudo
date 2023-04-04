from Textos import *
from Pokemon import *
from Treinadores import *
from locais import *
import random

cidade='Pallet'


def listaLocais(locais):
     n=0
     lista=[]
     if type(locais)==str:
         print(f'{1}--{locais}')
         lista.append(locais)
         valor=5-len(lista)
         for i in range(valor):
              lista.append('')
     else:
          for i in locais:
               n+=1
               lista.append(i)
               print(f'{n}--{i}')
          valor=5-len(lista)
          for i in range(valor):
              lista.append('')
     return lista



def opc(escolha,op1,op2,op3,op4,op5):
    if escolha=='1':
        return op1
    elif escolha=='2':
        return op2
    if escolha=='3':
        return op3
    elif escolha=='4':
        return op4
    elif escolha=='5':
        return op5

def Aventura(local):
    global cidade

    if Player.pokemons[0].hp<=0:
        print('Seus Pokemons estão machucados vá ao Centro Pokemon')
        opçõesCidade(cidade)

    cidades=['Pallet','Viridian','Pewter','Cerulean','Vermillion','Saffron','Celadon','Fuchsia','Lavender','Cinnabar']
    lista=listaLocais(local.rotas)
    num=input()

    Nome=opc(num,lista[0],lista[1],lista[2],lista[3],lista[4])
    if Nome not in cidades:
        rota=rotas(Nome)
        for i in range(random.randrange(4)):
            selvagem=NomePokemon(rota.selvagens)
            resultado=Player.batalha(selvagem)
        print(resultado)
        if resultado:
            cidade=Nome
            opçõesCidade(Nome)
        else:
            Explorar(cidade)
    else:
        cidade=Nome
        opçõesCidade(Nome)
    
        
def Explorar(cidade):
    print(f'''\t\t---Local atual: {cidade}   --- ''')
    cidades=['Pallet','Viridian','Pewter','Cerulean','Vermillion','Saffron','Celadon','Fuchsia','Lavender','Cinnabar']
    if cidade in cidades:
        match cidade:
            case "Pallet":
                Aventura(Pallet)

            case 'Viridian':
                Aventura(Viridian)

            case 'Pewter':
                Aventura(Pewter)
            
            case 'Cerulean':
                Aventura(Cerulean)

            case 'Vermilion':
                Aventura(Vermilion)
            
            case 'Saffron':
                Aventura(Saffron)

            case 'Celadon':
                Aventura(Celadon)

            case 'Fuchsia':
                Aventura(Fuchsia)
            
            case 'Cinnabar':
                Aventura(Cinnabar)
            
            case 'Lavender':
                Aventura(Lavender)
    else:
        rota=rotas(cidade)
        Aventura(rota)
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
        4-- Market
        5-- Opções''')
    match input(''):
        case '1':
            Explorar(Nome)
        case '2':
            Treinadores()
        case '3':
            Textos('Centro')
        case '4':
            Textos('Mark')
        case '5':
            Opcoes(0.05)



if Menu(0.05):
    print('''
    Seja Bem-Vindo a sua aventura pokemon, primeiro precisamos saber o seu Nome''')
    Nome=input('')
    Player=Jogador(Nome,dinheiro=500)
    while True:
        print(f'''\nBom {Nome} Para Começar Sua Aventura Escolha o seu primeiro Pokemon
        1-- Charmander
        2-- Squirtle
        3-- Bulbasaur\n''')
        try:
            op =int(input(''))
            if op>0 and op<=3:
                match op:
                    case 1:
                        Player.capturar('Charizard')
                    case 2:
                        Player.capturar('Squirtle')
                    case 3:
                        Player.capturar('Bulbasaur')
                opçõesCidade()
            else:
                print('Digite um Valor Valido')
        except:
            print('Digite um Valor Valido')
    
        
    
