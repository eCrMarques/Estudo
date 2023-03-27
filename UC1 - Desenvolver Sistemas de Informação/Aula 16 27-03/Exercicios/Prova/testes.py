from Textos import *
def vida(total, atual):
     vida=''
     vidaStr=str(atual)
     total=int(total/10)
     atual=int(atual/10)
     if total==atual:
          vida='/'*20+vidaStr+'/'*20
     else:
          porcentagem=int(total/atual)
          vida='/'*(20-int(20/porcentagem))+vidaStr+'-'*int(20/porcentagem)
     return f'[{vida}]'


