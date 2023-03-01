x=list(input(""))
y=['y','e','s']
n=['n','a','o']
p=0
print(x)
for i in x:
    p+1
    print(y[p])
    if(i==y[p]):
        print("Confirmado")
    else:
        if(i==n[p]):
            print("Cancelado")


