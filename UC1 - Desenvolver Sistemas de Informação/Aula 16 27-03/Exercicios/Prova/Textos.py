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
    imprimir('---------------Menu---------------\n\n'
          '  1- - -- ---New Game--- -- - -1\n'
          '        2--  -Opções- --2\n'
          '            3- Sair -3\n'
          ,velocidadeDoTexto)
    match int(input()):
        case 1:
            loop("--------Começando Jogo----------",1,0.077)
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

def Textos(Local):
    if Local==0:
        print('Seja Bem-Vindo ao Torneio Pokemon\n'
              'É a sua Primeira vez em um Torneio?')
        resposta=input()
        if resposta=='Sim':
            print(
            'Entendo, sendo assim você pode escolher entre um desses Pokemons para iniciar sua aventura\n'
            '(1)Charmander\n(2)Squirtle\n(3)Bulbasaur')
            pokemon = input()
            # Capturar(pokemon)
        elif resposta =='Não':
            print('Seja Bem-Vindo de Volta')

    elif Local==1:
        print('Torneio 1')

    elif Local==2:
        print('Torneio 2')

    elif Local==3:
        print('Torneio 3')
def lprint(texto):
    imprimir(texto,velocidadDoTexto)

def OpçõesLuta():
    lprint(f'1 -- Atacar\n'
                '2 -- Mochila\n'
                '3 -- Fugir\n')
    match int(input()):
        case 1:
            return True
        case 2:
            print('Mochila')
        case 3:
            print('Fugir')
    
