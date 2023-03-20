#Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche. 
#Considere que a cada execução somente será calculado um item.
dic={"cq":'100','bc':'101','bo':'102','h':'103','ch':'104','r':'105'}
v=0
while True:
    x =input("Item: ")
    if(x=='fim'):
        break
    try:
        q=int(input('Quantidade: '))
        if(x==dic['cq']):
            v= q*1.1
            print(f"{q} Cachorro Quente: {v} Reais")
        elif(x==dic['bc']):
            v= q*1.3
            print(f"{q} Bauru Simles: {v} Reais")
        elif(x==dic['bo']):
            v= q*1.5
            print(f"{q} Bauru c/ovo: {v} Reais")
        elif(x==dic['h']):
            v= q*1.1
            print(f"{q} Hamburguers: {v} Reais")
        elif(x==dic['ch']):
            v= q*1.3
            print(f"{q} Chesseburguer: {v} Reais")  
        elif(x==dic['r']):
            v= q*1
            print(f"{q} Refrigerante: {v} Reais")
    except Exception as e:
        print("Quantidade Invalida")