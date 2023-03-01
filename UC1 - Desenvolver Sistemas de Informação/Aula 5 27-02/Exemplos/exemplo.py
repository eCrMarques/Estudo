while True:
    Num =int(input("Digite um número inteiro: "))
    contador =0
    for i in range (1,Num+1):
        if Num%i==0:
            contador = contador+1
            print(i)
    if contador<=2:
        print(f"{Num} é Primo")
    else:
        print(f"{Num} não é Primo")
    if Num==0:
        break