import time
import random 

velocidadeDoTexto=0.005
def imprimir(texto,velocidadeDotexto,tipo=None):
    if tipo == None:
        tipo=True
    for x in texto:
        print(x,end='',flush=tipo)
        time.sleep(velocidadeDotexto)

def loop(texto,vezes,velocidadeDoTexto,fls=None):
    if fls==None:
        fls=True
    x=' '*len(texto)
    imprimir(texto,velocidadeDoTexto,tipo=fls)
    for i in range(vezes):
        imprimir(f'\r{x}',velocidadeDoTexto,tipo=fls)
        imprimir(f'\r{texto}',velocidadeDoTexto,tipo=fls)
       
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
                loop('Saindo....',1,0.06)
                exit()
            case _:
                print('Opção invalida')


def Textos(Local=None):
    match Local:
        case 'Centro':
            print('''Seja Bem-Vindo ao Centro Pokemon
Deseja Curar seus Pokemons?
            S/N
    Para Guardar/Trocar Digite (G)''')
            op=input()
            if op.lower()=='s':
                return 'Sim'
            elif op.lower()=='n':
                return 'Não'
            elif op.lower()=='g':
                return 'Guardar'
            else:
                return
        case 'Mark':
            print('''Seja Bem-Vindo ao Market
            Deseja Comprar items?\nS/N''')
            op=input()
            if op.lower()=='s':
                return 'Sim'
            elif op=='n':
                return 'Não'
            else:
                return

def lprint(texto):
    imprimir(texto,velocidadeDoTexto)

def Capturar(item):
    resultado=False
    match item:
        case 'Poke Ball':
            chance=random.randrange(3)
            print(chance)
            if chance==0:
                return True
        case 'Great Ball':
            chance=random.randrange(2)
            if chance==0:
                return True
        case 'Ultra Ball':
            chance=random.randrange(1)
            print(item, 'Usada')
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
     print('Digite qualquer tecla para Voltar')
     return lista

def Depot(Jogador):
    Centro=Jogador[1]
    if 'Pokemon' in str(type(Jogador[0])):
        Centro.append(Jogador[0])
        return Centro
    while True:
        print(f'Centro Pokemons Guardados')
        for i,pokemon in enumerate(Centro):
            print(f'{i+1:3}-||{pokemon.nome:12}||-', end='')
            if (i+1)%5==0:
                print('\n')
        if print(end=''):
            print('\n')
        print(f'\nMeus Pokemons')
        for i,pokemon in enumerate(Jogador[0].pokemons):
            print(f'{i+1:3}--{pokemon.nome:12}', end='')
        print("\n\nPara Guardar Insira o número do Pokemon\nTrocar insira (PokemonTime-PokemonGuardado)\nPegar Pokemon(-PokemonGuardado)\ts -- Sair",end='\n')
        op=input('')
        if op.lower() =='s':
            break
        else:
            if '-' in op:
                op=op.split('-')
                if op[0].isnumeric():
                    try:
                        meupokemon=Jogador[0].pokemons[int(op[0])-1]
                        Jogador[0].pokemons[int(op[0])-1]=Centro[int(op[1])-1]
                        Centro[int(op[1])-1]=meupokemon
                    except:
                        print('Valor Invalido')
                else:
                    if len(Jogador[0].pokemons)<6 and len(Centro)>0 and int(op[1])<=len(Centro):
                        Jogador[0].pokemons.append(Centro[int(op[1])-1])
                        Centro.pop(int(op[1])-1)
                    else:
                        print('Não é Possivel ')
            else:
                try:
                    if len(Jogador[0].pokemons)==1 or int(op)>len(Jogador[0].pokemons):
                        print('\nNão é Possivel Ficar Sem Pokemon')
                        input()
                    else:
                        Centro.append(Jogador[0].pokemons[int(op)-1])
                        Jogador[0].pokemons.pop(int(op)-1)
                except:
                    print("Valor invalido")
    return Centro
            


