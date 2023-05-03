import psycopg2
from Controle.ConexãoClass import Conexão
from Modelo.classAluguél import Aluguel
from Modelo.classCliente import Cliente
from Modelo.classLivro import Livro

def Atualizar(tipo):
    Visualizar(tipo)
    dados=conexaoBanco.consultarBanco(f"""
    select * from "{tipo}" """)
    id=input(f"Digite o Id do {tipo}")
    if int(id) in [item[0] for item in dados]:
        if tipo == "Cliente":
            NovoCliente=Cliente(id,input("Digite O Nome: "),input("Telefone Ex:(123456789): "), input("Cpf: "))
            conexaoBanco.manipularBanco(NovoCliente.atualizar())
        elif tipo =="Livro":
            NovoLivro=Livro(id,input("Digite O Nome: "),input("Quantidade: "), input("Data Lançamento Ex(Ano-Mês-Dia): "))


    

def Excluir(tipo):
    id=input(f"Id do {tipo}: ")
    try:
        conexaoBanco.Excluir(tipo,id)
    except:
        print("Dados Não Encontrados")
    

def AdicionarLivro():
    
    NovoLivro=Livro(None,input("Digite O Nome: "),input("Quantidade: "), input("Data Lançamento Ex(Ano-Mês-Dia): "))
    try:
        conexaoBanco.manipularBanco(NovoLivro.inserirLivro())
    except:
        print('Invalido')

def AdicionarCliente():
    
    NovoCliente=Cliente(None,input("Digite O Nome: "),input("Telefone Ex:(123456789): "), input("Cpf: "))
    try:
        conexaoBanco.manipularBanco(NovoCliente.inserirCliente())

    except:
        print('Invalido')

def AdicionarAluguel():
    print('----Cliente----')
    Visualizar('Cliente')
    print('----Livros----')
    Visualizar('Livro')
    
    livro=input("Digite o id do Livro: ")
    quantidade=conexaoBanco.consultarBanco(f"""Select "Quantidade" from "Livro" where "id_Livro" = '{livro}' """)[0][0]
    if quantidade==0:
        print("Livro Indisponivel")
    else:
        NovoAluguel=Aluguel(None,input("Digite o id do Cliente: "),livro,None)
        try:
            conexaoBanco.manipularBanco(NovoAluguel.inserirAluguel())
            conexaoBanco.manipularBanco(NovoAluguel.Retirar(quantidade))
        except:
            print('Invalido')

def Visualizar(tipo,pos=None):
    if pos==None:
        Lista=conexaoBanco.consultarBanco(f"""
        Select * from "{tipo}"
        """)
    else:
        Lista=conexaoBanco.consultarBanco(f"""
        Select * from "{tipo}" where "id_{tipo}" = '{pos}'
        """)
    Nome='Nome'
    Lançamento='Lançamento'
    Quantidade='Quantidade'

    if tipo =='Cliente':
        Lançamento='Telefone'
        Quantidade='Cpf'
    
    elif tipo =='Aluguel':
        Lançamento='Livro'
        Quantidade='Entregue'
        Nome = 'Cliente'
    
    for item in Lista:
        print(f'Id: {item[0]}  {Nome}: {item[1]} {Lançamento}: {item[2]} {Quantidade}: {item[3]}')
while True:
    try:
        conexaoBanco=Conexão("Livraria","localhost","5432","postgres","postgres")
        op = input('''
        1- Ver Livros
        2- Ver Clientes
        3- Alugar Livro
        4- Adicionar 
        5- Remover
        6- Sair   
        ''')

        match op:
            case '1':
                Visualizar('Livro')
            case '2':
                Visualizar('Cliente')
            case '3':
                AdicionarAluguel()
                Visualizar('Aluguel')
                op=input("Ver Mais informação s/n: ")
                if op=='s':
                    op=input('Mais informação insira o id Cliente-Livro (x-y)')
                    op=op.split('-')
                    print('---Cliente---')
                    Visualizar('Cliente',op[0])
                    print('---Livro---')
                    Visualizar('Livro',op[1])
                    input()
                
            case '4':
                op= input('1-Adicionar Livro \n2-Adicionar Cliente\n')
                match op:
                    case '1':
                        AdicionarLivro()
                    case '2':
                        AdicionarCliente()
            case '5':
                op=input("\t-Remover-\n1-Cliente\n2-Livro\n")
                match op:
                    case '1':
                        Excluir("Cliente")
                    case '2':
                        Excluir("Livro")
                    case _:
                        print()
                print("Excluido")
                        
            case '6':
                break
            case _:
                print("Opção Incorreta")
                Atualizar("Cliente")

    except(psycopg2.Error,Exception) as error:
        print("Conexão Erro ", error)

