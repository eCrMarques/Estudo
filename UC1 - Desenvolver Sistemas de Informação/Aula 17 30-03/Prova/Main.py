from Pokemon import *
from Treinadores import *
Local=0

if Menu(0.005):
    if Local==0:
        Nome=print(input('\nQual o seu Nome?\n'))
        Inicial=0
        match Textos(Local):
                case 1:
                    Inicial='Charmander'
                case 2:
                    Inicial= 'Squirtle'
                case 3:
                    Inicial= 'Bulbasaur'
        Nome=Jogador(Nome,Inicial,dinheiro=500)
print(Nome.__dict__)