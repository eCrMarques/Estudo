lista =[1,2,3]
tupla = (1,2,3)
dicionario ={"Nome":'Cristian'}
conjunto ={}

print("Teste Lista")
print(lista)
print(lista[2])
lista[2]= 33

print(lista[2])

print("Teste Tupla")
print(tupla)
print(tupla[2])

# tupla[2] = 33    ----Não mutavel
# print(tupla[2])

print('Teste Dicionario')
print(dicionario)
print(dicionario["Nome"])

dicionario["Nome"] = "Emanuel"
print(dicionario)
