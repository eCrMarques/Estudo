#1 para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
def q1(n):
    for i in range(n):
        print(n)


#2 para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
def q2(n):
    for i in range(1,(n+1)):
        print(i)

#3 Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def soma(p,s,t):
    print(int(p)+int(s)+int(t))

#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def Pn(x):
    if x<=0:
        return 'N'
    else:
        return 'P'
print(Pn(-5))
#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo
#que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.