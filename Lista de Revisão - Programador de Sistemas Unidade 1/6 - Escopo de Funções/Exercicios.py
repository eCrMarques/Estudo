# Escopo de Funções


# 1. Escreva um programa que solicite ao usuário dois números e imprima a soma, a
# subtração, a multiplicação e a divisão desses números. Crie funções separadas para
# cada operação matemática.
def Questão1():
    def soma(num1,num2):
        return num1+num2
    def subtração(num1,num2):
        return num1-num2
    def multiplicação(num1,num2):
        return num1*num2
    def divisão(num1,num2):
        return num1/num2
    num=input('Exemplo: 1+1  1-1  1*1  1/1\nInsira um Calculo contendo dois Números: ')
    if '+' in num:
        num =num =num.split('+')
        print(soma(int(num[0]),int(num[1])))
    elif '-' in num:
        num =num.split('-')
        print(subtração(int(num[0]),int(num[1])))
    elif '*' in num:
        num =num.split('*')
        print(multiplicação(int(num[0]),int(num[1])))
    elif '/' in num:
        num =num.split('/')
        print(divisão(int(num[0]),int(num[1])))


# 2. Escreva um programa que solicite ao usuário um número e imprima se esse número
# é par ou ímpar. Crie uma função para determinar se um número é par e outra função
# para determinar se um número é ímpar.
def Questão2():
    def par(Valor):
        if Valor%2==0:
            return True
    def impar(Valor):
        if Valor%2!=0:
            return True
    numero=int(input("Informe um Número: "))
    if par(numero):
        print(f'{numero} É par')
    if impar(numero):
        print(f'{numero} É Impar')


# 3. Escreva uma função que receba uma lista de números inteiros como parâmetro e
# retorne a média dos números. A função deve verificar se a lista está vazia e retornar
# None caso esteja. Em seguida, utilize uma variável global para contar quantas vezes
# a função foi chamada e imprimir o valor da contagem ao final de cada chamada.
listaInteiros=[2,3,4,1,8,5,6,3,2,10]
listaVazia=[]
chamadaQ3=0
def Questão3(lista):
    global chamadaQ3
    if len(lista)==0:
        chamadaQ3+=1
        return None
    else:
        chamadaQ3+=1
        return sum(lista)/len(lista)

while chamadaQ3<5:
    print(f'{Questão3(listaInteiros)}\na Função Foi Chamada {chamadaQ3} vezes')

# 4. Escreva uma função que calcule o fatorial de um número inteiro n. A função deve
# utilizar uma variável local para armazenar o resultado e uma estrutura de repetição
# para calcular o fatorial. Em seguida, utilize uma variável global para contar quantas
# vezes a função foi chamada e imprimir o valor da contagem ao final de cada
# chamada.
chamadaQ4=0
# def Questão4():
#     numero=int(input("Digite um Valor:"))
#     def fatorial(Valor):
#         resultado=1
#         global chamadaQ4
#         for i in range(1,Valor+1):
#             resultado=resultado*i
#         chamadaQ4+=1
#         return resultado
#     print(f'fatorial de {numero} é : {fatorial(numero)}\nfoi chamada {chamadaQ4} vezes')

# while chamadaQ4<5:
#     Questão4()

# 5. Escreva uma função que receba uma lista de strings como parâmetro e retorne a
# string com o maior número de caracteres. A função deve utilizar uma variável local
# para armazenar a string com o maior número de caracteres e uma estrutura de
# repetição para percorrer a lista. Em seguida, utilize uma variável global para contar
# quantas vezes a função foi chamada e imprimir o valor da contagem ao final de cada
# chamada.
listaString=['a','ab','abc','abcd','k','jhkl','kh','jkhlg']
chamadaQ5=0
def Questão5(lista):
    def maiorString(string):
        maior=len(lista[0])
        if len(string)>maior:
            maior= len(string)
        return maior
    for item in listaString:
        print(maiorString(item))

Questão5(listaString)   