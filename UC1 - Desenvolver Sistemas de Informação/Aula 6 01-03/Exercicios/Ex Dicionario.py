#1. Escreva um script Python para classificar (crescente e decrescente) um dicionário por valor
def q():
    d={"B":5,'E':2,'C':3,'D':4}
    d= sorted(d.items())
    print(d)
    print(d[::-1])
def q6():
    s =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    p=[]
    for i in s:
        p.append(i[::-1])
    p= sorted(p)
    s.clear()
    print(p)
    for i in p:
        s.append(i[::-1])
    print(s)
