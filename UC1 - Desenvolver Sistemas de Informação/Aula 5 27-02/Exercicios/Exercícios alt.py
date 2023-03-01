#Dado o nome de uma pessoa, retorne o número de letras do nome e a primeira letra do nome.
def nome():
    c=0
    nam =input("Nome: ")
    for l in nam:
        if l!=" ":
            c =c +1
    print('Quantidade de Letras:',c,'\nPrimeira Letra',nam[0])
nome()
#Dada uma palavra, retorna a palavra invertida
def invertido():
    nam= input("Palavra: ")
    print(nam[::-1])
invertido()
#Dada uma palavra, retorna os caracteres nas posições ímpares
def impares():
    p=input("Palavra: ")
    for i in range(len(p)):
        if i%2==0:
            print(p[i] ,'posição', (i+1),'Impar')
impares()