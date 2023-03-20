#Dado o nome de uma pessoa, retorne o número de letras do nome e a primeira letra do nome.
def  nome():
    nome= input("Nome: ")
    qnt = len(nome)- nome.count(" ")
    print('A Quantidade de Letra é: ',qnt,'\n Primeira Letra: ',nome[0])
#Dada uma palavra, retorna a palavra invertida
def inverse():
    n =input("Palavra: ")
    print(n[::-1])
#Dada uma palavra, retorna os caracteres nas posições ímpares
def posiçãoImpar():
    p =input("Palavra: ")
    x=0
    for i in p:
        x+=1
        if x%2!=0:
            print(i, 'Posição: ' ,x)

list=['asd','jkl','uio']
print(list)
print("".join(list[::-1]))

p = input("Palavra:")
for i in range(0,len(p),2):
    print(p[i],(i+1),"Posição")