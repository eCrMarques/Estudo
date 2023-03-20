"""(Sem estruturas de repetição)
Faça um programa que peça 5 itens e suas respectivas
quantidades e mostre na tela a lista de itens com a quantidade,
Item 1 – Quantidade: V
Item 2 – Quantidade: W
Item 3 – Quantidade: Y
Item 4 – Quantidade: X
Item 5 – Quantidade: Z"""

item =[]
qntd =[]
x=0

for i in range(5):
    itemx=input("Digite O Nome: ")
    item.append(itemx) 
    qntdx=input("Digite a Quantidade: ")
    qntd.append(qntdx)
for z in range(5):
    x= x+1
    print(f"Item {x}: {item[z]} Quantidade: {qntd[z]}")
