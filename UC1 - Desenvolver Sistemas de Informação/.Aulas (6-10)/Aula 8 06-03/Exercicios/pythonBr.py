#1 para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
def q1(n):
    p= ""
    for i in range(1,n+1):
        p = str(i)*i
        print(str(p))

q1(10)
#2 para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
def q2(n):
    p= ""
    for i in range(1,n+1):
        p = p+str(i)
        print(str(p))
q2(10)
#3 Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def soma(p,s,t):
    print(int(p)+int(s)+int(t))

#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def Pn(x):
    if x<=0:
        return 'N'
    else:
        return 'P'

#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo
#que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
def somaimposto(taxa,custo):
    valor = (taxa/100)*custo+custo
    return valor
print(somaimposto(10,100))

# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. 
# como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
def conv(hr):
    hr =int(hr)-12
    return hr
def main():
    time = input('Hora: ')
    time = time.split(':')
    if int(time[0])>24 or int(time[0])<0:
        print('Hora Invalida')
    elif int(time[0])>60 or int(time[1])<0:
        print('Minutagem Invalida')
    elif int(time[0])>12:
        print(f'{conv(time[0])}:{time[1]} P.M')
    elif int(time[0])<12:
        print(f'{time[0]}:{time[1]} A.M')
    elif int(time[0])==12:
        print(f'{time[0]}:{time[1]} P.M')
    elif int(time[0])==00:
        print(f'{time[0]}:{time[1]} A.M')
       


# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
# O programa deverá então exibir o valor a ser pago na tela.
# Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
# O cálculo do valor a ser pago é feito da seguinte forma. 
# Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valor,atrasos):
    if atrasos ==0:
        return valor
    else:
        resultado = (valor*0.03)+(atrasos*(0.001*valor))
        return valor+resultado
# vl = int(input("Digite o Valor: "))
# at = int(input('Digite a quantidade de dias atrasados: '))

# print(valorPagamento(vl,at))

# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def qntd(b):
    return len(str(b))

# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def rev(a):
    a= str(a)
    return a[::-1]

# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
def verify(d,m,a):
    if int(d)<1 or int(d)>30:
        print("Dia Invalido")
    elif int(m)<1 or int(m)>12:
        print('Mês Invalido')
    else:
        return "valido"
def meses(n):
    n-=1
    meses=('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
    return meses[n]
def main():
    data=input("Digite a Data em Formato DD/MM/AAAA: ")
    data = data.split('/')
    if verify(data[0],data[1],data[2]) == "valido":
        print(f'{data[0]} de {meses(int(data[1]))} de {data[2]}')
    
#Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
# Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante
x = int(input("Tamanho Linha: "))
y = int(input('Tamanho Coluna: '))
for i in range(y+1):
    if i ==0 or i== y:
        r='-'
        r=r*(x-2)
        print(f'+{r}+')
    else:
        r=' '
        r=r*(x-2)
        print(f'|{r}|')
