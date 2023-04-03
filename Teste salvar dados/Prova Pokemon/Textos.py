import time
import random 

velocidadeDoTexto=0.005
def imprimir(texto,velocidadeDotexto):

    for x in texto:
        print(x,end='',flush=True)
        time.sleep(velocidadeDotexto)

def loop(texto,vezes,velocidadeDoTexto):
    x=' '*len(texto)
    imprimir(texto,velocidadeDoTexto)
    for i in range(vezes):
        imprimir(f'\r{x}',velocidadeDoTexto)
        imprimir(f'\r{texto}',velocidadeDoTexto)
       
def Menu(velocidadeDoTexto):
    while True:
        print('---------------Menu---------------\n\n'
            '  1- - -- ---New Game--- -- - -1\n'
            '        2--  -Sair- --2\n'
            )
        match input():
            case '1':
                loop("--------Começando Jogo----------",1,0.027)
                return True
            case '2':
                exit
            case _:
                print('Opção invalida')

def Opcoes(velocidadeDoTexto):
    imprimir('1- -- ---Velocidade De Texto--- -- -1\n'
               '     2- -- -Voltar- -- -2\n'
           ,velocidadeDoTexto)
    match input():
        case '1':
            match velocidadeDoTexto:
                case 0.01:
                    VTexto='Medio'
                case 0.005:
                    VTexto='Rapido'
                case 0.06:
                    VTexto='Lento'
            imprimir(f'        Velocidade Atual: {VTexto}\n'
                  f'             Alterar Para\n 1-Lento -- 2-Medio  -- 3-Rapido\n'
                  ,velocidadeDoTexto)
            match input():
                case '1':
                    velocidadeDoTexto=0.06
                case '2':
                    velocidadeDoTexto=0.01
                case '3':
                    velocidadeDoTexto=0.005
                case _:
                    print('Opção Inexistente')
            Opcoes(velocidadeDoTexto)

        case '2':
            Menu(velocidadeDoTexto)
        case _:
            print('Opção Inexistente')
            Opcoes(velocidadeDoTexto)

def Textos(Local=None):
    match Local:
        case 'Centro':
            print('''Seja Bem-Vindo ao Centro Pokemon
            Deseja Curar seus Pokemons?''')
            op=input()
            if op=='Sim':
                return 'Sim'
            elif op=='Não':
                return 'Não'
            else:
                return
        case 'Mark':
            print('''Seja Bem-Vindo ao Market
            Deseja Comprar items?''')
            op=input()
            if op=='Sim':
                return 'Sim'
            elif op=='Não':
                return 'Não'
            else:
                return

def lprint(texto):
    imprimir(texto,velocidadeDoTexto)

def Capturar(item):
    resultado=False
    match item:
        case 'Poke ball':
            chance=random.randrange(3)
            if chance==0:
                return True
        case 'Great Ball':
            chance=random.randrange(2)
            if chance==0:
                return True
        case 'Ultra Ball':
            chance=random.randrange(1)
            print(item)
            if chance==0:
                return True

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

