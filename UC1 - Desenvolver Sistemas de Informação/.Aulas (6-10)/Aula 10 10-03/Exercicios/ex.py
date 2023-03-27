# Construa um algoritmo para ler um número inteiro, positivo de três dígitos, e gerar outro número formado pelos dígitos invertidos do número lido. 
#  Ex: 
# NumeroLido = 123 
# NumeroGerado = 321 
# Dica: Observe os resultados das funções Quociente e Resto de um número por 10.
def inv():
    x = int(input('Digite um Valor de 3 digitos: '))
    a=int((x-x%100+x%10-x%10)/100)
    b=int((x%100-x%10)/10)
    c=int(x%10)
    print(f'{c}{b}{a}')


# Elabore um algoritmo que receba como entrada o valor do saque realizado pelo cliente de um banco e 
# retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 reais. 
def cont(n):
    notas=('100','50','20','10','5','2','1')
    t =[0,0,0,0,0,0,0]
    if n>=100:
        t[0]=(int(n/100))
        n= n-int(t[0]*100)
    elif n>=50:
        t[1](int(n/50))
        n= n-int(t[1]*50)
    elif n>=20:
        t.append(int(n/20))
        n= n-int(t[2]*20)
    elif n>=10:
        t.append(int(n/10))
        n= n-int(t[3]*10)
    elif n>=5:
        t.append(int(n/5))
        n= n-int(t[4]*5)
    elif n>=2:
        t.append(int(n/2))
        n= n-int(t[5]*2)
    elif n>=1:
        t.append(int(n/1))
        n= n-int(t[6]*1)
    print(t)
cont(1455)
        
        





