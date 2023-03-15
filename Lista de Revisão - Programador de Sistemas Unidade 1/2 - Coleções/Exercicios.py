# Coleções


# 1. Escreva um programa que leia uma lista de números inteiros e imprima o maior e o
# menor número da lista.
def Questão1():
    lista=[]
    for i in range(4):
        lista.append(int(input("Digite um Valor:")))
    print(f'Menor Número é: {min(lista)}\nMaior Número é: {max(lista)}')


# 2. Escreva um programa que leia uma lista de nomes e crie um dicionário onde a
# chave é o nome e o valor é o número de vezes que o nome aparece na lista.
def Questão2():
    lista=['Emanuel','Emanuel','Cristian','Cristian','Cristian','Teste']
    dicionario={}
    for nome in set(lista):
        dicionario[nome]=nome
        dicionario[nome] = lista.count(nome)
    print(dicionario)


# 3. Escreva um programa que leia uma lista de números inteiros e remova todos os
# valores duplicados. Em seguida, imprima a lista sem os valores duplicados.
def Questão3():
    lista=[1,2,3,4,5,6,7,8,9,1,2,3,1,2,4,1]
    lista=set(lista)
    lista=list(lista)
    print(lista)
