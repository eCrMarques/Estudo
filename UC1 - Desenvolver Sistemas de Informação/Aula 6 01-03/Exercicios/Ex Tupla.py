# Tupla 
#1 Write a Python program to create a tuple
#3 Write a Python program to create a tuple of numbers and print one item.
def q2():
    n=[]
    for i in range(3):
        i = input()
        n.append(i)
    n=tuple(n)
    print(n)
    print(type(n))
    print(n[1])

#4 Write a Python program to unpack a tuple into several variables
#6 Write a Python program to convert a tuple to a string
def q4():
    t=('um','dois','três','quatro')
    for i in t:
        i=i
        print(i,type(i))

#5 Write a Python program to add an item to a tuple
#11 Escreva um programa Python para converter uma lista em uma tupla
def q6():
    n=("a","b",'c','d')
    print(n,type(n))
    ad= input("Adicionar a tupla:")
    n=list(n)
    n.append(ad)
    n=tuple(n)
    print(f"{n}'\n'{type(n)}")

#7 Write a Python program to get the 4th element from the last element of a tuple.
def q7():
    n=('q','w','e','r','t')
    print(n[1::-3])

#9. Escreva um programa Python para localizar itens repetidos em uma tupla
def q8():
    t=('q','w','e','r','q','w')
    n=-1
    for i in t:
        n+=1
        if t.count(i)>1:
            print(f'{i} Posição {n}')

#10 Escreva um programa Python para verificar se existe um elemento dentro de uma tupla
#14. Escreva um programa Python para encontrar o índice de um item em uma tupla
def q9():
    t=('q','w','e','r')
    x =input("Letra: ")
    if x in t:
        print(x,'Esta contido')
    else:
        print(x,'Não Esta contido')    

#12. Escreva um programa Python para remover um item de uma tupla     
def q11():
    t=('q','w','e','r')
    x =input("Remover: ")
    if x in t:
        t= list(t)
        t.remove(x)
        t=tuple(t)
        print(t, type(t))
    else:
        print(x,'Não existe ')

#15. Escreva um programa Python para encontrar o comprimento de uma tupla.
def q12():
    t=('q','w','e','r')
    print(f'tamanho: {len(t)}')
