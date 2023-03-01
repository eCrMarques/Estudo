#1. Escreva um programa em Python para somar todos os itens de uma lista.
def soma():
    num=[1,2,3,4,7,8,4,3,1]
    soma=0
    for n in num:
        soma=soma+n
    print(soma)
#2. Escreva um programa em Python para multiplicar todos os itens de uma lista
def multi():
    num=[1,8,4,3,1,5,6,4]
    m=1
    for n in num:
        m = m*n
    print(m)
#3. Escreva um programa em Python para obter o maior número de uma lista.
def maior():
    num=[1,5,4,3,2,1,8,7,9,4,15,13,17,11]
    c=num[0]
    for n in num:
        if n>c:
            c=n
    print(c)
#4. Escreva um programa Python para obter o menor número de uma lista
def menor():
    num=[-1-5,-7,-3,1,0,5,4,7]
    c=num[0]
    for n in num:
        if n<c:
            c=n
    print(c)
#5. Escreva um programa Python para contar o número de strings de uma determinada lista de strings.
#O comprimento da string é 2 ou mais e o primeiro e o último caractere são os mesmos. 
# Ir para o editor Lista de amostras: ['abc', 'xyz', 'aba', '1221'] Resultado esperado: 2
def equal():
    i=0
    x=['abc','xyz','aba','1221']
    for l in x:
        if len(list(l))>2 and l[0] ==l[-1]:
            i=i+1
            print(l)

    print('Resultado:',i)
#6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# Go to the editor Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def ultCrescente():
    i=0
    m=[]
    li=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
    sorted((2, 5), (1, 2), (4, 4), (2, 3), (2, 1))
        

ultCrescente()