import time
def printLento(texto,velocidadeDotexto=0.1):
    for x in texto:
        print(x,end='',flush=True)
        time.sleep(velocidadeDotexto)

def apagar(b):
    a=' '*(len(b))
    printLento(f'\r{a}')

def Loading(load,velocidadeDotexto,qntd):
        a='/'*(len(load))
        printLento(f'[{load}]',0.001)
        printLento(f'\r[{a}]')
        printLento(f'\r[{load}]')
        

Loading('-----------------------------',0.1,3)
    

# Loading('.....Carregando.....')