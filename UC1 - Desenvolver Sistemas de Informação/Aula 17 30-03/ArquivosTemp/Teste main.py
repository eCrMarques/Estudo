from Textos import *
from Pokemon import *
from Treinadores import *
Nome=print(input('\nQual o seu Nome?\n'))
Player=Jogador(Nome,dinheiro=500)
match Textos(0):
        case '1':
            Player.capturar('Charmander')
        case '2':
            Player.capturar('Squirtle')
        case '3':
            Player.capturar('Bulbasaur')
print(Player.pokemons)
