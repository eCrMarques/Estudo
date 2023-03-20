num = int(input("Digite um Valor: "))
primo =True
for i in range(2,num):
    if num%i==0:
        primo =False
if primo:
    print('é primo')
else:
    print('não é primo')