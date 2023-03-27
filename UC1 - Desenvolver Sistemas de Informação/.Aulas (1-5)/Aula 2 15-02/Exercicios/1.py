#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
while True:
    A =int(input("Digite o Valor de A: "))
    B =int(input("Digite o Valor de B: "))
    C =int(input("Digite o Valor de C: "))

    if ((A+B)<C):
        print("Menor que C")
    elif(A+B==C):
        print("Igual")
        break
    else:
        print("Maior que C")
