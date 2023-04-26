from Controle.classConexão import Conexão
from Modelo.classCliente import Cliente
from Modelo.classCompra import Compra
from Modelo.classProduto import Produto
import psycopg2

def cadastrarCliente():
    clienteNovo=Cliente(None,input('Insira o Nome: '))
    
    conexãoBanco.manipularBanco(clienteNovo.inserirCliente())
    
    print("Cliente Cadastrado com Sucesso")

def cadastrarProduto():
    ProdutoNovo=Produto(None,input('Insira o Nome: '),input('Insira o Preço: '),input('Insira o Estoque: '))
    
    conexãoBanco.manipularBanco(ProdutoNovo.inserirProduto())

    print("Produto Cadastrado com Sucesso")

def cadastrarCompra():
    cliente,idproduto,quantidade=input("Id Cliente: "),input("Id Produto: "),input("Quantidade: ")
    Total=Produtos[int(idproduto)-1].preço*int(quantidade)
    CompraNova=Compra(None,cliente,idproduto,quantidade,Total,None)

    if Produtos[int(idproduto)-1].estoque>int(quantidade):
        conexãoBanco.manipularBanco(CompraNova.InsirarCompra(Total))
        conexãoBanco.manipularBanco()
    else:
        print('Compra encerrada')

try:
    conexãoBanco = Conexão("Loja","localhost","5432","postgres","postgres")
    Produtos=[Produto(produto[0],produto[1],produto[2],produto[3]) for produto in conexãoBanco.consultarBanco("""Select * from "Produto" """)]
    Clientes=[[client[0],client[1]] for client in conexãoBanco.consultarBanco("""Select * from "Cliente" """)]
    for produto in Produtos:
        print(produto.__dict__)
        
    cadastrarCompra()

except (psycopg2.Error,Exception) as error:
    print("Falha ", error)



    # conexãoBanco.manipularBanco("""
    # CREATE TABLE "Compra"(
    # "Id_Compra" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # "Id_Cliente" int,    FOREIGN KEY ("Id_Cliente")      REFERENCES "Cliente"("Id_Cliente"),
    # "Id_Produto" int, FOREIGN KEY ("Id_Produto") REFERENCES "Produto"("Id_Produto"),
    # "Quantidade" int NOT NULL default '0',
    # "Valor_Total" numeric NOT NULL default '0',
    # "TimeStamp" TIMESTAMP NOT NULL DEFAULT CURRENT_DATE
    # )
    # """)