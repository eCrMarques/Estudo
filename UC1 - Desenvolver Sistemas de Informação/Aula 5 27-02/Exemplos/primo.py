x = int(input("Numero: "))
for i in range(0,x,1):
    if x%i==0 or x==1:
        p="Não é Primo"
        break
    else:
        p="Primo"
print(p)