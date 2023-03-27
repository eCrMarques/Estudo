def hello(nome):
    print('Hello',nome)
hello("Cristian")
def Pagamento(qtdHoras,valorHoras):
    if qtdHoras<=40:
        Salario = qtdHoras*valorHoras
    else:
        exc=qtdHoras-40
        Salario= 40*valorHoras+(exc*(1.5*valorHoras))
    return Salario
salario =Pagamento(41,30)
print(salario)


lista =[4,7,2,1,9,4,3]
print(sorted(lista))
print(lista.sort())

print(lista)


#imc
def imc(peso,altura):
    print(peso/altura**2)
imc(78,1.78)