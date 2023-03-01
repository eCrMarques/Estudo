Frutas=['Abacate','Berinjela','Laranja','Manga','Banana']
print(type(Frutas))
def comandos():
    print(Frutas)

    print("Len:",len(Frutas))

    print("3 Posição:",Frutas[3])

    Frutas[4] ="Cenoura"
    print("Alteração Banana > Cenoura\n",Frutas)

    Frutas.append("Abacaxi")
    print("Adicionando Abacaxi\n",Frutas)

    Frutas.insert(4,"Caju")
    print("Inserindo Caju no 4 lugar\n",Frutas)

    Frutas.pop(5)
    print("Removendo objeto do 5 Lugar\n",Frutas)

    Frutas.remove("Berinjela")
    print("Removendo Item Berinjela:\n",Frutas)

f =input("Nome: ")
if f in Frutas:
    print("Esta na Lista")
else:
    print("Não esta na Lista")
for fruta in Frutas:
    if f ==fruta:
        print("Esta Na Lista")

for i in range(len(Frutas)):
    if f== Frutas[i]:
        print(f,"Esta na posição", i)
