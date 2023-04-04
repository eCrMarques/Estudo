from locais import *
novaCidade='Pallet'
cidade=novaCidade
def listaLocais(locais):
     lista=[]
     if type(locais)==str:
         lista=f'{1}--{locais}'
     else:
          for i in locais:
               n=+1
               lista.append(f'{n}--{i}')
     return lista
def Explorar():
    print(f'''\t\t---Local atual: {cidade}--- ''')
    n=0
    match cidade:
        case "Pallet":
            print(listaLocais(Pallet.rotas))
            op=input()
            if op==1:
               global novaCidade
               novaCidade='Viridian'
        case 'Viridian':
            locais=['Rota Liga Pokemon','Floresta de Viridian']


Explorar()
