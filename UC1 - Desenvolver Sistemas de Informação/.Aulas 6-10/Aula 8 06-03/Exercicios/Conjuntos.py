#19. Write a Python program to calculate the difference between the two lists.
l1 =[1,2,3,4,5,6]
l2 =[2,4,6,8,10,12]
for l in l1:
    if l not in l2:
        print(l,'Não está contido em L2')
print(list(set(l1)-set(l2)))

#20. Escreva um programa Python para acessar o índice de uma lista.
x=-1
for n in l2:
    x+=1
    print(n, 'Posição:',x)