#Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche. 
#Considere que a cada execução somente será calculado um item.
dic={"100":{"p":'1.1',"n":"Cachorro Quente"},
     '101':{"p":1.3,"n":"Bauru simples"},
     '102':{"p":1.5,"n":"Bauru c/ovo"},
     '103':{"p":'1.1',"n":"Hamburger"},
     '104':{"p":'1.3',"n":"Cheeseburger"},
     '105':{"p":'1',"n":"Refrigerante"}}

x =input("Item: ")
if dic.get(x):
    q=int(input('Quantidade: '))
    if type(q)==int:
        total= float(dic[x]["p"])*q
        nome= dic[x]["n"]
        print(total,nome)
    else:
        print("Quantidade Invalida")
else:
    print("Codigo invalido")