import time
velocidadeDoTexto=0.01

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
          '        2--  -Opções- --2          \n'
          '            3- Sair -3             \n'
          ,velocidadeDoTexto)
    match int(input()):
        case 1:
            loop("--------Começando Jogo----------",1,0.073)
        case 2:
            Opcoes(velocidadeDoTexto)
        case 3:
            exit

def Opcoes(velocidadeDoTexto):
    imprimir('1- -- ---Velocidade De Texto--- -- -1\n'
               '  2   - -- -Excluir Salvo- -- -2\n'
          '          3-   Salvar   -3           \n'
          '            4 -Sair- 4\n',velocidadeDoTexto)
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
            pass
        case 4:
            Menu(velocidadeDoTexto)


