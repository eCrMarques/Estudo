user ={"Nome":'Emanuel',"Ultimo Nome":"Cristian","Idade":"20",'Curso':"Py","Endereço":"Pi"}


print(user.items())
print(f'Nome: {user["Nome"]}')
print(f'Ultimo Nome: {user["Ultimo Nome"]}')
print(f'Idade: {user["Idade"]}')
print(f'Curso: {user["Curso"]}')
print(f'Endereço: {user["Endereço"]}')

del(user["Curso"])
user["Nome"] = "Lopes"

print(user.items())
print(user["Endereço"])

user2 = user.copy()

user2["Nome"] = "Oliver"
user2["Idade"] = 30

print(user2)