import random
v =int(random.uniform(1,100))
p=0
while p !=v:
    try:
        x = input('Insira um Palpite: ')
        x=int(x)
        p=x
        if x > v :
            print('Menor ')
            print(v)
        elif x < v:
            print('Maior')
            print(v)
        elif x == v:
            break
    except:
        if ',' in x and type(x)!= type(int):
            x= x.split(',')
            if v in range(int(x[0]),int(x[1])):
                print(f'Esta entre {x[0],x[1]}')
                print(v)
            else:
                print(f'Não Esta entre {x[0],x[1]}')
                print(v)
