#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá somar os dois, caso contrário multiplique A por B. 
# Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

while True:
    a =int(input("Valor de A: "))
    b =int(input("Valor de B: "))
    if(a==b):
        c= a+b
    else:
        c= a*b
    print(c)
    if(a==0):
        break