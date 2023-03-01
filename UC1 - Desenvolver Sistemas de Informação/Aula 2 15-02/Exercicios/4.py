#Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.
b =0
c =0
p= 0
for i in range(3):
    x =int(input("Digite um valor: "))
    if(x>b):
        if(b!=0):
            b =x
            p= p+1
        elif(b==0):
            b =x
            p=1  
    if(p>1):
        c ==x
    
            
print(b,c)
    

