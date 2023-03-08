# Criar um programa calculadora
    # Receber Dois números e uma operação (+,-,/,*)
    # Dependendo da operação escolhida, passa os números para uma das funções.
    # No Final imprime o resultado ea função escolhida.

# Criar função para Soma
# Criar função para Subtração
# Criar função para Multiplicação
# Criar função para Divisão

def soma(a,b):
    r=int(a)+int(b)
    return r

def subtração(a,b):
    r=int(a)-int(b)
    return r

def multi(a,b):
    r=int(a)*int(b)
    return r

def divi(a,b):
    r=int(a)/int(b)
    return r

def main():
    x=input("")
    try:
        if '+' in x:
            x= x.split('+')
            print(soma(x[0],x[1]))
        elif '-' in x:
            x= x.split('-')
            print(subtração(x[0],x[1]))
        elif '/' in x:
            x= x.split('/')
            print(divi(x[0],x[1]))
        elif '*' in x:
            x= x.split('*')
            print(multi(x[0],x[1]))
        else:
            print('Valor Invalido')
    except:
        try:
            x[0]=int(x[0])
            print("Operador Invalido")
        except:
            print("Valor Invalido")
        
while True:
    main()

    