import random
from Dex import Pokedex
import Pokemon
import time
velocidadeDoTexto=0.01
def printLento(texto,velocidadeDotexto):
    for x in texto:
        print(x,end='',flush=True)
        time.sleep(velocidadeDotexto)

def Menu():
    printLento('---------------Menu---------------\n\n'
          '  1- - -- ---New Game--- -- - -1\n'
          '        2--  -Opções- --2          \n'
          '            3- Sair -3             \n'
          ,velocidadeDoTexto)
    match int(input()):
        case 1:
            print("Começando Jogo")
        case 2:
            Opcoes()
        case 3:
            exit

def Opcoes():
    global velocidadeDoTexto
    printLento('1- -- ---Velocidade De Texto--- -- -1\n'
               '  2   - -- -Excluir Salvo- -- -2\n'
          '            3- Voltar -3             \n',velocidadeDoTexto)
    match int(input()):
        case 1:
            match velocidadeDoTexto:
                case 0.01:
                    VTexto='Medio'
                case 0.005:
                    VTexto='Rapido'
                case 0.06:
                    VTexto='Lento'
            printLento(f'        Velocidade Atual: {VTexto}\n'
                  f'             Alterar Para\n 1-Lento -- 2-Medio  -- 3-Rapido\n'
                  ,velocidadeDoTexto)
            match int(input()):
                case 1:
                    velocidadeDoTexto=0.06
                case 2:
                    velocidadeDoTexto=0.01
                case 3:
                    velocidadeDoTexto=0.005
            print(velocidadeDoTexto)
            Opcoes()
        
        case 2:
            pass
        case 3:
            Menu()
Opcoes()


