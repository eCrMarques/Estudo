# Ler do teclado um número inteiro e imprimir se ele é primo ou não.
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