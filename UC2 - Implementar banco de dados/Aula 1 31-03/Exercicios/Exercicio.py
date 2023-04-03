# Instruções:

# Crie um menu com as opções "Visualizar Funcionarios" e "Cadastrar Funcionarios".
# Ao escolher a opção "Cadastrar Funcionarios", o usuário deve ser solicitado a inserir as informações do funcionário, como nome, idade e cargo.
# As informações do funcionário devem ser armazenadas em um arquivo JSON separado.
# Ao escolher a opção "Visualizar Funcionarios", o sistema deve ler o arquivo JSON e exibir as informações de cada funcionário cadastrado na tela.
# O sistema deve continuar rodando até que o usuário escolha a opção de saída.

# Dica: Para ler e escrever informações em um arquivo JSON em Python, você pode usar a biblioteca integrada json. Para exibir informações na tela, use a função print(). Para criar um loop que continue rodando até que o usuário escolha a opção de saída, você pode usar um loop while.

# Desafio:

# Crie a funcionalidade de remover um funcionário
# Crier a funcionalidade de atualizar um funcionário
import json
def Salvar(novalista):
    with open('Funcionario.json','w') as Funcionariojson:
        json.dump(novalista,Funcionariojson,indent=2)

def Atualizar():
    with open('Funcionario.json','r') as Funcionarios:
        Lista=json.load(Funcionarios)
        return Lista

def VerFuncionario():
     Lista=Atualizar()
     print('Nome\tCpf\tSalario\tDepartamento')
     for funcionario in Lista:
        print(f'{funcionario["Nome"]}\t{funcionario["Cpf"]}\t{funcionario["Salario"]}\t{funcionario["Departamento"]}')
    
def CriarFuncionario():
    novoFuncionario={}
    novoFuncionario["Nome"]=input('Digite Seu Nome:')
    novoFuncionario["Cpf"]=input('Digite Seu cpf:')
    novoFuncionario["Salario"]=input('Digite Seu Salario:')
    novoFuncionario["Função"]=input('Digite Seu Função:')
    novoFuncionario["Departamento"]=input('Digite Seu Departamento:')

    novaLista = Atualizar()
    novaLista.append(novoFuncionario)   
    
    with open('Funcionario.json','w') as Funcionariojson:
        json.dump(novaLista,Funcionariojson,indent=2)
        

def RemoverFuncionario():
    nome =input('Porfavor Digite O Nome Do Funcionario')
    lista=Atualizar()
    Contem=True

    for i in range(len(lista)):
        if nome==lista[i]["Nome"]:
            Contem=True
            posição=i
        else:
            Contem=False

    if Contem:
        lista.pop(posição)
        Salvar(lista)
    else:
        print('Funcionario Inexistente')


while True:
    print("""
            1 -- Visualizar Funcionarios
            2 -- Cadastrar Funcionario
            3 -- Remover Funcionario
            0 -- Sair""")
    op=input()
    match op:
        case '1':
            VerFuncionario()
        case '2':
            CriarFuncionario()
        case '3':
            RemoverFuncionario()
        case '0':
            print('-----Saindo----')
            break


