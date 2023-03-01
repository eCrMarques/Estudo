x=[]
for i in range(3):
    v=int(input("Numero: "))
    x.append(v)
a=x[0]
b=x[1]
c=x[2]
if a!=b and b!=c:
    if a>b:
        if b>c:
            primeiro =a
            segundo =b
            terceiro =c
        elif b<c:
            if a>c:
                primeiro =a
                segundo =c
                terceiro =b
            else:
                primeiro =c
                segundo =a
                terceiro =b
    if a<b:
        if b<c:
            primeiro =c
            segundo =b
            terceiro =a
        elif b>c:
            if a>c:
                primeiro =b
                segundo =a
                terceiro =c
            else:
                primeiro =b
                segundo =c
                terceiro =a
    print(primeiro,segundo,terceiro)
else:
    print("Números Iguais")
