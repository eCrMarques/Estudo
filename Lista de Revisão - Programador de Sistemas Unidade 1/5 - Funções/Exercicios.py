# Funções


# 1. Escreva uma função que receba uma lista de números inteiros e retorne o maior
# número da lista.
listaInteiros=[1,2,3,4,8,6,1,2,5,3]
def Questão1(lista):
    return max(lista)
print(Questão1(listaInteiros))


# 2. Escreva uma função que receba uma lista de palavras e retorne uma lista contendo
# apenas as palavras que começam com a letra "a".
listaPalavras=['Guarda-Chuva','Roupa','Armario','Laranja','Azul','Paleta','amarelo']
def Questão2(lista):
    listaA=[]
    for item in lista:
        item =item.lower()
        if item[0] =='a':
            listaA.append(item.capitalize())
    return listaA
print(Questão2(listaPalavras))


# 3. Escreva uma função que receba uma lista de números inteiros e retorne a soma dos
# números pares da lista.
listaNumeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def Questão3(lista):
    soma=0
    for num in lista:
        if num%2==0:
            soma=soma+num
    return soma
print(Questão3(listaNumeros))


# 4. Escreva uma função que receba uma lista de dicionários contendo informações
# sobre pessoas (nome, idade, cidade) e retorne uma lista contendo apenas os nomes
# das pessoas que moram em uma cidade específica.

listaDicionario=[{'Nome':'Cristian','idade':'20','Cidade':'Fortaleza'},{'Nome':'João','idade':'19','Cidade':'Fortaleza'},{'Nome':'Pedro','idade':'25','Cidade':'Caucaia'}]
def Questão4(lista):
    listaD=[]
    for item in lista:
        if item['Cidade'] =='Caucaia':
            for chave in item.keys():
                listaD.append(item[chave])
            listaD.append('-')
    return listaD
print(Questão4(listaDicionario))


