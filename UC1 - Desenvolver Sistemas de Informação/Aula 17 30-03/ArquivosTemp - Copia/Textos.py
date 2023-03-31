import time
velocidadDoTexto=0.005
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
    print('---------------Menu---------------\n\n'
          '  1- - -- ---New Game--- -- - -1\n'
          '        2--  -Opções- --2\n'
          '            3- Sair -3\n'
          ,velocidadeDoTexto)
    match int(input()):
        case 1:
            # loop("--------Começando Jogo----------",1,0.027)
            return True
        case 2:
            Opcoes(velocidadeDoTexto)
        case 3:
            exit

def Opcoes(velocidadeDoTexto):
    imprimir('1- -- ---Velocidade De Texto--- -- -1\n'
               '     2- -- -Excluir Salvo- -- -2\n'
          '         3- - Voltar - -3\n'
           ,velocidadeDoTexto)
    match int(input()):
        case 1:
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
            match int(input()):
                case 1:
                    velocidadeDoTexto=0.06
                case 2:
                    velocidadeDoTexto=0.01
                case 3:
                    velocidadeDoTexto=0.005
            Opcoes(velocidadeDoTexto)
        
        case 2:
            pass
        case 3:
            Menu(velocidadeDoTexto)

def Textos(Local=None):
    match Local:
        case 'Centro':
            print('''Seja Bem-Vindo ao Centro Pokemon
            Deseja Curar seus Pokemons?''')
            op=input()
            if op=='Sim':
                curarPokemons()
            else:
                print('''Negar Centro''')
        case 'Mark':
            print('''Seja Bem-Vindo ao Market
            Deseja Comprar items?''')
            op=input()        
            if op=='Sim':
                print('items')
            else:
                print('''Negar Market''')
def lprint(texto):
    imprimir(texto,velocidadDoTexto)

def OpçõesLuta():
    lprint(f'1 -- Atacar\n'
                '2 -- Mochila\n'
                '3 -- Time\n'
                '4 -- Fugir\n')
    num=input()
    try:
        num=int(num)
        if num<5:
            match num:
                case 1:
                    return True
                case 2:
                    print('Mochila')
                case 3:
                    print("Time")
                case 4:
                    print('Fugir')
        else:
            print('Valor invalido')
    except:
        print('Valor Invalido')

# print('----Você Deseja-----\nComeçar o Torneio\nExplorar e se Aventurar\nIr no Centro Pokemon\nIr no Market')
# opção=int(input())
# if opção==1:
#     opção=int(input('Torneios\n'))
#     Textos(opção)
