# Deve conter as seguintes entidades Funcionarios e Departamentos
# Requisitos: 
# - Ver lista de funcionarios
# - Ver lista de departamentos
# - Ver informações de funcionarios especificos (Deve conter o Departamento de que faz parte)
# - Ver lista de funcionarios de um departamento específico
# - Opcional: Funcionário gerente e autenticação antes de usar o sistema
# - Inserção de Funcionários e Departamentos
# - Atualização de informações de Funcionários e Departamentos
# - Remoção de Funcionários e Departamentos

# Entidade Funcionários:

# Id_Func: integer AUTO GENERATED (PK)
# Nome_Func: var char(255) NOT NULL
# Salário_Func: float(2) NOT NULL default 0.00
# Cargo_Func: char(255) NOT NULL default Autônomo
# Id_Departamento: integer (FK)

# Entidade Departamento:

# Id_Dept: integer AUTO GENERATED (PK)
# Nome_Dept: char(255) 
# Id_Gerente: integer (FK)

import psycopg2

#Funções devem ser rodadas apenas uma vez

def criarTabelaFuncionario():
    sql="""
    CREATE TABLE "Funcionarios" (
    "Id_Func" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome_Func" varchar(255) NOT NULL,
    "Salário_Func" money NOT NULL default 0,
    "Cargo_Func" varchar(255) NOT NULL default 'Autonomo',
    "Id_Dept" int NOT NULL default 1
    )
    """
    return sql

def criarTabelaDepartamentos():
    sql="""
    CREATE TABLE "Funcionarios" (
    "Id_Dept" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome_Dept" varchar(255) NOT NULL,
    "Id_Gerente" int NOT NULL default 1

    )
    """
    return sql

def verFuncionarios(id=None):
    if id==None:
        cursor.execute("""
        Select * from "Funcionarios"
        """)

        for Funcionario in cursor.fetchall():
            print(f'Id: {Funcionario[0]:<3} Nome: {Funcionario[1]:<15}')
    else:
        cursor.execute(f"""
        Select * from "Funcionarios" where "Id_Func"={id}
        """)
        for Funcionario in cursor.fetchall():
            print(f'Id: {Funcionario[0]:<3} Nome: {Funcionario[1]:<15} Salario: {Funcionario[2]:<15} Cargo: {Funcionario[3]:<15} Departamento {Funcionario[4]:<3}')

def verDepartamentos(id=None):
    if id==None:
        cursor.execute("""
        Select * from "Departamentos"
        """)
        for Departamento in cursor.fetchall():
            print(f'Id:{Departamento[0]:<3} Nome: {Departamento[1]:<3} Gerente: {Departamento[2]:<3}')
        
    else:
        cursor.execute(f"""
        Select * from "Departamentos" where "Id_Dept"={id}
        """)
        for Funcionario in cursor.fetchall():
            print(f'Id: {Funcionario[0]:<3} Nome: {Funcionario[1]:<15} Salario: {Funcionario[2]:<15} Cargo: {Funcionario[3]:<15} Departamento {Funcionario[4]:<3}')

def alterar():
    padrao=['"Nome_Func"','"Salário_Func"','"Cargo_Func"','"Id_Dept"']
    verFuncionarios()
    id=f"'{input('Id: ')}'"
    verFuncionarios(id)
    nome=f"'{input('Insira o Nome: ')}'"
    salario=f"'{input('Insira o Salario: ')}'"
    cargo=f"'{input('Insira o Cargo: ')}'"
    idDep=f"'{input('Insira o Id Departamento: ')}'"
    
    for i,item in enumerate((nome,salario,cargo,idDep)):
        if item =="''":
            item=padrao[i]


    sql=f"""
    Update "Funcionarios"
    set 
    "Nome_Func"= {nome},
    "Salário_Func"= {salario},
    "Cargo_Func"= {cargo},
    "Id_Dept" = {idDep}
    where
    "Id_Func"={id}
    """

    return sql

def criarFuncionario():
    nome=input("Insira o Nome")
    salario=input("Insira o Salario")
    cargo=input("Insira o Cargo")
    idDep=input("Insira o Id Departamento")

    nome=f"'{nome}'"
    salario=f"'{salario}'"
    cargo=f"'{cargo}'"
    idDep=f"'{idDep}'"

    for func in (nome,salario,cargo,idDep):
        if func=='':
            func='default'
    sql= f"""Insert into "Funcionarios" Values(default,{nome},{salario},{cargo},{idDep}) 
    
    """
    return sql

def criarDepartamento():
    nome=f"'{input('Informe o Nome do Departamento: ')}'"
    Gerente=f"'{input('Informe o Id do Gerente: ')}'"

    sql = f"""
    insert into "Departamentos" values(default,{nome},{Gerente})"""
    return sql
gerente=[]
def verificação():
    global gerente
    print(gerente)
    if gerente==[]:
        gerente=input("Insira uma senha ")
        print("Senha criada com sucesso")
        return False
    else:
        pwd=input("Insira uma Senha:")
        if pwd in [gerente]:
            return True
        else:
            print('Senha errada')
            return False

try:
    conn = psycopg2.connect(dbname="Empresa1",
    host="localhost", port="5432", user="postgres", password="postgres"
                        )
    cursor= conn.cursor()

    while True:
        print(f'''
        1- Ver Funcionarios
        2- Ver Departamentos
        3- Inserir Funcionario/Departamento
        4- Sair''')
        match input():
            case '1':
                verFuncionarios()
                op=input('1-Procurar por Id\n2-Alterar')
                if op=='1':
                    id=f"'{input('Id do Funcionario: ')}'"
                    verFuncionarios(id)
                elif op=='2':
                    try:
                        cursor.execute(alterar())
                    except(Exception,psycopg2.Error) as error:
                        print(f'Valor incorreto {error}')
            case '2':
                verDepartamentos()
                op=input('1-Procurar por Id\n')
                if op=='1':
                    id=f"'{input('Id do Funcionario: ')}'"
                    verDepartamentos(id)
            case '3':
                    
                    if verificação():
                        op=input('1- Funcionario \n2- Departamento')
                        match op:
                            case '1':
                                cursor.execute(criarFuncionario())
                                conn.commit()
                                print("Funcionario criado com Sucesso")
                            case '2':
                                cursor.execute(criarDepartamento())
                                conn.commit()
                                print("Departamento criado com Sucesso")
                    else: 
                        pass
            case '4':
                break

    

    # cursor.execute(criarTabelaFuncionario())
    # conn.commit()
    # print("Tabela Funcionario com Sucesso")

    # cursor.execute(criarTabelaDepartamentos())
    # conn.commit()
    # print("Tabela Departamento com Sucesso")


except(Exception,psycopg2.Error) as error:
    print("Não conectado", error)