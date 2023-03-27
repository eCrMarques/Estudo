#Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre 
#Calcular a sua média (aritmética), informar o nome e sua menção aprovado (media >= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9)

while True:
    p=[]
    v,z=0,0
    nome=input("Escreva Seu Nome: ")
    for i in range(3):
        z= z+1
        x=float(input(f"Nota {z}°: "))
        p.append(x)
        v= p[i] +v
    m= v/3
    print(v,m)
    if(m>=7):
        print("Aprovado")
    if(m<=5):
        print("Reprovado")
    if(m>5 and m<=7):
        print("Recuperação")
    if(x==0):
        break