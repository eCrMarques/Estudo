# Tipos de Dados


# 1. Escreva um programa que solicite ao usuário um número inteiro e imprima o dobro
# desse número.
def Questão1():
    try:
        num = int(input('Digite um Número Inteiro: '))
        print(f'O Dobro de {num} é: {num*2}')
    except:
        print("Valor Invalido")


# 2. Escreva um programa que solicite ao usuário o raio de um círculo e calcule a área
# desse círculo.
def Questão2():
    try:
        raio=float(input("Insira o valor do Raio: "))
        print(f'A área do Circulo de Raio {raio} é aproximadamente: {(raio*raio)*3.14} ')
    except:
        print("Valor Invalido")


# 3. Escreva um programa que solicite ao usuário seu nome e idade e imprima uma
# mensagem personalizada com essas informações.
def Questão3():
    Nome=input('Informe seu Nome: ')
    idade=int(input('Informe sua Idade: '))
    if idade<15 :
        print(f'{Nome}, Você é uma Criança')
    elif idade>=15 and idade<18 :
        print(f'{Nome}, Você é um Adolescente')
    elif idade>=18 and idade<28 :
        print(f'{Nome}, Você é um Jovem-Adulto')
    elif idade>=28 and idade<70 :
        print(f'{Nome}, Você é um Adulto')
    elif idade>=70 and idade<113 :
        print(f'{Nome}, Você é um Jovem de Mente, com um Corpo cansado')
    elif idade>=113:
        print('Você Conseguiu')
