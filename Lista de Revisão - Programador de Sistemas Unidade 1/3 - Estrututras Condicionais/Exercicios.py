# Estruturas Condicionais


# 1. Escreva um programa que solicite ao usuário um número e imprima se ele é
# positivo, negativo ou zero.
def Questão1():
    try:
        num=float(input("Digite um Valor: "))
        if num>0:
            print(f'{num} é Positivo.')
        elif num<0:
            print(f'{num} é Negativo.')
        elif num==0:
            print(f'{num} é Zero.')
    except:
        print("Digite um Valor Númerico")


# 2. Escreva um programa que leia o nome e a idade de uma pessoa e imprima uma
# mensagem personalizada com base na idade. Se a idade for menor que 18 anos,
# imprima "Você é menor de idade". Se a idade estiver entre 18 e 65 anos, imprima
# "Você é adulto". Caso contrário, imprima "Você é idoso".
def Questão2():
    nome=input('Insira o Nome: ')
    idade=int(input('Insira a Idade: '))
    if idade<18:
        print(f'{nome},Você é Menor de Idade')
    elif idade>=18 and idade<=65:
        print(f'{nome},Você é Adulto')
    else:
        print(f'{nome},Você é Idoso')


# 3. Escreva um programa que solicite ao usuário a nota de um aluno em uma prova e
# imprima a mensagem "Aprovado" se a nota for maior ou igual a 7, "Reprovado" se a
# nota for menor que 5 e "Recuperação" se a nota estiver entre 5 e 7.
def Questão3():
    nota=float(input('Insira a Nota: '))
    if nota>=7:
        print('Aprovado')
    elif nota<5:
        print('Reprovado')
    elif nota>=5 and nota<7:
        print('Recuperação')


# 4. Escreva um programa que solicite ao usuário a idade e o sexo de uma pessoa e
# imprima uma mensagem personalizada com base nas seguintes condições:
# ● Se a pessoa for do sexo feminino e tiver menos de 25 anos, imprima "Você é
# uma jovem mulher".
# ● Se a pessoa for do sexo feminino e tiver 25 anos ou mais, imprima "Você é
# uma mulher adulta".
# ● Se a pessoa for do sexo masculino e tiver menos de 25 anos, imprima "Você
# é um jovem homem".
# ● Se a pessoa for do sexo masculino e tiver 25 anos ou mais, imprima "Você é
# um homem adulto".
def Questão4():
    idade =int(input('Digite Sua Idade: '))
    sexo =input('Informe-nos o seu Sexo(M ou F): ')
    sexo =sexo.lower()
    if sexo =='m':
        if idade<25:
            print('Você é um Jovem Homem')
        elif idade>=25:
            print('Você é um Homem Adulto')
    elif sexo =='f':
        if idade<25:
            print('Você é um Jovem Mulher')
        elif idade>=25:
            print('Você é um Mulher Adulta')

