# A realização de 4 questões, de forma correta, dessa seção isentam o aluno de ter que realizar as outras seções.


# 1. Escreva uma função que receba como parâmetro uma lista de números inteiros e
# retorne a soma dos números pares na lista. Em seguida, utilize um laço de repetição
# para solicitar ao usuário uma lista de números inteiros, chame a função e imprima o
# resultado.
lista1=[]
for i in range(4):
    lista1.append(int(input('Numero à adicionar na lista: ')))

soma=0
for item in lista1:
    if item%2==0:
        soma=soma+item
print(f'O resultado da soma é: {soma}')




# 2. Escreva uma função que receba como parâmetro uma string e verifique se a string é
# um palíndromo (ou seja, pode ser lida da mesma forma de trás para frente). Em
# seguida, utilize uma estrutura de repetição para solicitar ao usuário uma string,
# chame a função e imprima se a string é um palíndromo ou não.

def Questão2(string):
    global chamadaQ2
    chamadaQ2+=1
    if string == string[::-1]:
        print('É um Palindromo')
    else:
        print('Não é um Palindromo')

chamadaQ2=0
while chamadaQ2<5:
    str=input('Digite uma palavra: ')
    Questão2(str)

# 3. Escreva uma função que receba como parâmetro uma lista de strings e retorne a
# quantidade de strings que possuem mais de 5 caracteres. Em seguida, utilize uma
# estrutura condicional para perguntar ao usuário se ele deseja adicionar mais strings
# à lista, e utilize um laço de repetição para solicitar ao usuário as novas strings,
# chame a função e imprima o resultado.
listaString=['skj','sfjg','kfhajd','asd','fj','k','slçk']
def Questão3(lista):
    listaGeral=[]
    for item in lista:
        if len(item)>5:
            listaGeral.append(item)
    print(f'Lista contém {len(listaGeral)} items com 5+ caracteres')
    for item in listaGeral:        
        print(f'{item} contem mais de 5 caracteres:')

    if input('Deseja Adicionar Mais strings?: ') =='Yes':
        quantidade = int(input('Quantas Strings: '))
        for i in range(quantidade):
            string=input(f'String {i+1}°: ')
            listaGeral.append(string)
        Questão3(listaGeral)

Questão3(listaString)



# 4. Escreva uma função que receba como parâmetro uma lista de números inteiros e
# retorne o número máximo na lista. Em seguida, utilize uma estrutura de repetição
# para solicitar ao usuário uma lista de números inteiros, chame a função e imprima o
# resultado. Se a lista estiver vazia, a função deve retornar None e o programa deve
# imprimir uma mensagem informando que a lista está vazia.



# 5. Escreva uma função que receba como parâmetro um número inteiro n e retorne uma
# lista com os n primeiros números da sequência de Fibonacci. Em seguida, utilize
# uma estrutura condicional para perguntar ao usuário se ele deseja gerar a sequência 
# de Fibonacci para outro número, e utilize um laço de repetição para solicitar ao
# usuário os novos valores de n, chame a função e imprima o resultado.
num = int(input("Gere a Sequencia Fibonacci até a posição: "))
def Questão5(numero):
    fibonacci=[1,1]
    for i in range(1,numero-1):
        fibonacci.append((fibonacci[i-1])+fibonacci[i])
    print(fibonacci[0:numero])

Questão5(num)