#Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar.
while True:
    n =int(input("Numero: "))
    if(n%2==0):
        print("Par")
    else:
        print("Impar")
    if n==0:
        break