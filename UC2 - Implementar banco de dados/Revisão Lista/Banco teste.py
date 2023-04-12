# Agora, vocês serão dividos aleatoriamente em duplas. Vocês enviarão a
# documentação criada para seu parceiro e receberão a documentação
# criada por ele. Sua tarefa é criar uma aplicação Python capaz de ler o
# JSON do colega e exibi
# r as seguintes informações:
# 1. Lista de funcionários
# 2. Lista de departamentos
# 3. Informações específicas de um funcionário (por exemplo, o nome,
# idade e cargo de um funcionário com um determinado ID)
# 4. Quais funcionários fazem parte de um departamento específico
# (por exemplo, listar os funcionários que pertencem ao
# departamento de Desenvolvimento)
# Dicas:
# ● Use a biblioteca json do Python para ler o arquivo JSON.
# ● Crie funções separadas para cada uma das informações
# solicitadas.
# ● Use a estrutura de dados adequada para implementar as funções
# de busca e filtragem necessárias

import json

with open('dados.json','r') as dados:
    lista=json.load(dados)

def Funcionarios(id=None,qntd=None):
    if id==None:
        for funcionario in lista['funcionarios']:
            print(f'Id:{funcionario["id"]:<4}Nome:{funcionario["nome"]:<10}Cargo:{funcionario["cargo"]:<15}Id_Departamento:{funcionario["id_departamento"]:<10} ')
    else:
        for funcionario in lista['funcionarios']:
            if int(id)==funcionario["id"]:
                print(f'Id:{funcionario["id"]:<4}Nome:{funcionario["nome"]:<10}Cargo:{funcionario["cargo"]:<15}Id_Departamento:{funcionario["id_departamento"]:<10} ')
                break
    if qntd=='Todos':
        for funcionario in lista['funcionarios']:
            if funcionario["id_departamento"]==int(id):
                print(f'Id:{funcionario["id"]:<4}Nome:{funcionario["nome"]:<10}Cargo:{funcionario["cargo"]:<15}Id_Departamento:{funcionario["id_departamento"]:<10} ')
def Departamentos(id=None):
    if id==None:
        for departamento in lista['departamentos']:
            print(f'Id:{departamento["id"]:<4}Nome:{departamento["nome"]:<15}Descrição:{departamento["descricao"]:<10}')
    else:
        for departamento in lista["departamentos"]:
            if int(dp)==departamento["id"]:
                print(f'Id:{departamento["id"]:<4}Nome:{departamento["nome"]:<15}Descrição:{departamento["descricao"]:<10}\n')
while True:
    print("""
        1-Ver Funcionarios
        2-Ver Departamentos
        3-Procurar Funcionario
        4-Funcionarios por Departamentos""")
    opção=input()
    match opção:
        case '1':
            print('--------Funcionarios---------')
            Funcionarios()
            input()
        case '2':
            print('--------Departamentos---------')
            Departamentos()
            input()
        case '3':
            id=input('Id do Funcionario: ')
            if id.isnumeric()==False or int(id)>len(lista['funcionarios']):
                print('Id indisponivel ou Inexistente')
            else:
                Funcionarios(id)
            input()
        case '4':
            dp=input("Id do Departamento: ")
            if dp.isnumeric()==False or int(dp)>len(lista['departamentos']): 
                print("Id indisponivel ou inexistente")
            else:
                Departamentos(dp)
                Funcionarios(dp,'Todos')
            input()
        case _:
            break