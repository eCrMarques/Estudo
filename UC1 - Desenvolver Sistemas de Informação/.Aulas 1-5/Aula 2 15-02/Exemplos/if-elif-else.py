while True:
    idade =int(input("Digite sua Idade: "))
    if(idade>=10 and idade<20):
        print("Você é Adolescente")
    elif(idade>=20 and idade<30):
        print("Você é Jovem")
    elif(idade>=30 and idade<100):
        print("Você é Adulto")
    else:
        print("Valor Não Encontrado")
    if(idade<10):
        break