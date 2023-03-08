# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 >721
def rev(a):
    a= str(a)
    return a[::-1]
#print(rev(1234))

def qntd(b):
    return len(str(b))
#print(qntd(1234))

def pot(a,b):
    r=1
    for i in range(b):
        r=r*a
    return(r)
print((pot(2,4)))