#Tabuada
def tabuada():
    x =int(input("Tabuada do número: "))
    p=1
    for i in range(10):
        p=i+1
        s=x*p
        print(f'13 x {p} = {s}')
#Ler 10 numeros e Quantidade de numero entre 10 e 50
def entre():
    v=0
    for i in range(10):
        p=i+1
        x=int(input(f"Digite o {p}°: " ))
        if(x>=10 and x<=50):
            v=v+1
    print(v)
#Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.
def mValor():
    m=0
    for i in range(1,6):
        x =int(input(f"Digite o {i}° Número: "))
        if(m==0):
            m=x
        if(x<m):
            m=x
    print(m)
#Calcule o somatório dos números de 1 a 100 e imprima o resultado.
def Somatorio1():
    x=0
    for i in range(1,101):
        x+=i
    print(f"O Somatorio de 1 a 100 é igual a: {x} ")
#Ler do teclado um número inteiro e imprimir se ele é primo ou não.
def nprimo():
    while True :
        x = int(input("Digite um Numero: "))
        if (x<8):
            if x==2:
                print("Primo")
            elif x==3:
                print("Primo")
            elif x==5:
                print("Primo")
            elif x==7:
                print("Primo")
            else:
                print("Não é primo")
        elif (x>=8):
            if x%2 ==0:
                print("Não é primo")
            elif x%3 ==0:
                print("Não é primo")
            elif x%5 ==0:
                print("Não é primo")
            elif x%7 ==0:
                print("Não é primo")
            else:
                print("Primo")
        elif x==0:
            break
