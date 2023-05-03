import psycopg2
from Controle.ConexãoClass import Conexão

try:
    conexaoBanco=Conexão("Livraria","localhost","5432","postgres","postgres")
    
    # conexaoBanco.manipularBanco("""
    # CREATE TABLE "Livro"(
    # "id_Livro" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # "Nome_Livro" varchar(255) NOT NULL default 'Não Informado',
    # "Lançamento_Livro" DATE NOT NULL default CURRENT_DATE,
    # "Quantidade" varchar(3) NOT NULL default '1'
    # )
    #     """)
    
    # conexaoBanco.manipularBanco("""
    # CREATE TABLE "Cliente"(
    # "id_Cliente" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # "Nome_Cliente" varchar(255) NOT NULL default 'Não Informado',
    # "Telefone_Cliente" char(9) NOT NULL default 99999-9999,
    # "Cpf_Cliente" char(11) NOT NULL default '1111111111111'
    # )
    #     """)

    conexaoBanco.manipularBanco("""
    CREATE TABLE "Aluguel"(
    "id_Aluguel" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "id_Cliente" int, FOREIGN KEY ("id_Cliente") REFERENCES "Cliente"("id_Cliente"),
    "id_Livro" int, FOREIGN KEY ("id_Livro") REFERENCES "Livro"("id_Livro"),
    "Entregue" DATE NOT NULL default CURRENT_DATE
    )
        """)
except(psycopg2.Error,Exception) as error:
    print("Conexão Erro ", error)

