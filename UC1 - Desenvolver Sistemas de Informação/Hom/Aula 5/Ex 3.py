# Dada uma palavra, retorna os caracteres nas posições ímpares

nm = list(input("Digite uma Palavra: "))
x =0
for lt in nm:
    x = x+1
    if (x%2 ==0):
        pass
    else:
        print(lt, "Posição", x)
