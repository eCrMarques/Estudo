#Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche. 
#Considere que a cada execução somente será calculado um item.
dic={"100":'cq','101':'bc','102':'bo','103':'h','104':'ch','105':'r'}
v=0
while True:
    x =input("Item: ")
    if(x=='fim'):
        break
    try:
        q=int(input('Quantidade: '))
        if(x==dic['100']):
            v= q*1.1
            print(f"{q} Cachorro Quente: {v} Reais")
        elif(x==dic['101']):
            v= q*1.3
            print(f"{q} Bauru Simles: {v} Reais")
        elif(x==dic['102']):
            v= q*1.5
            print(f"{q} Bauru c/ovo: {v} Reais")
        elif(x==dic['103']):
            v= q*1.1
            print(f"{q} Hamburguers: {v} Reais")
        elif(x==dic['104']):
            v= q*1.3
            print(f"{q} Chesseburguer: {v} Reais")  
        elif(x==dic['105']):
            v= q*1
            print(f"{q} Refrigerante: {v} Reais")
    except Exception as e:
        print(e)