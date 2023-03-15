# Estruturas de Repetição


# 1. Escreva um programa que imprima todos os números ímpares entre 1 e 50.
def Questão1():
    for i in range(1,51,2):
        print(i)


# 2. Escreva um programa que leia uma lista de números inteiros e imprima a média
# desses números.
def Questão2():
    lista=[1,2,3,4,6,5,4,2,3,5]
    soma=0
    divisão=0
    for num in lista:
        soma=soma+num
        divisão+=1
    print(f'a média de é {soma/divisão}')


# 3. Escreva um programa que solicite ao usuário um número e imprima a tabuada desse
# número até o valor 10.
def Questão3():
    num=int(input('Digite um Número: '))
    print(f'-----------TABUADA DE {num} -----------')
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')


# 4. Escreva um programa que solicite ao usuário um número e imprima todos os
# números primos menores que esse número.
def Questão4():
    num =int(input('Insira um Valor: '))
    for i in range(num):
        if i==2 or i==3 or i==5 or i==7:
            print(i)
        elif i>=10:
            if i%2==0 or i%3==0 or i%5==0 or i%7==0:
                pass
            else:
                print(i)
