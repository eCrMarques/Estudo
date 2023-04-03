import json
class A:
    def __init__(self,a,b,c,d,e) -> None:
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e

h=A('fasdf','hfd','jhgfjhf','jhgk','jgwqweqwflj')
d=A('jkghjk','ghdfsdfg','gsdfg','jkçkjlç','jhkgh')
e=A('gfjhfghj','asdfasd','zxdz','yuity','jgasdasflj')
i=A('yityiryi','bvnvbmn',',mnb,bn','rwer',',m.k')
lista=[h,d,e,i]
with open ('Teste.json','r') as arquivo:
    e=json.load(arquivo)
a=''
def salvar():
    with open ('Save.json','w') as arquivo:
        x=['asda','hjfkhj','5564',546]
        w=[]
        n=-1
        pokemon=[]
        for item in lista:
            for objeto in item.__dict__.values():
                w.append(objeto)
            pokemon.append(list(w))
            w.clear()
            print(pokemon)
        y={}
        y['Nome']=x[0]
        y['Valor']=x[3]
        y['Cidade']=x[2]
        y['Pokemons']=pokemon
        json.dump(y,arquivo,indent=2)
salvar()
