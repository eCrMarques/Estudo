#Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.
def letras(l):
    x =('kjfghdflkghsdfah')
    print(f'{x.count(l)}')
letras('h')

#Faça uma função que receba uma lista de números armazenados de forma crescente, e dois valores ( limite inferior e limite superior)
#e exiba a sublista cujos elementos são maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.
teste=[0,4,9,4,6,15,18,30,25,41,32,12,8,5,4,95,13]
teste.sort()
def alc(lista,me,ma): 
    novaLista=[]
    for n in lista:
        if n >=me and n<=ma:
            novaLista.append(n)
    print(novaLista)
alc(teste,10,20)