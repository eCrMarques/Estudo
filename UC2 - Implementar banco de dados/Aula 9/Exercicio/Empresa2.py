import psycopg2

# Funcionarios:

# Func_id - int GENERATED ALWAYS AS IDENTITY PRIMARY KEY
# Func_nome - varchar(255)
# Func_cpf - char(11) #UNIQUE NOT NULL#
# Func_salario - money
# Dept_id - int
# CONSTRAINT fk_departamento
#   FOREIGN KEY ("ID_Dept")
#   REFERENCES "Departamento"("ID")
#   ON DELETE CASCADE, SET NULL, SET DEFAULT, NO ACTION
#   ON UPDATE NO ACTION

# Departamentos:

# Dept_id - int GENERATED ALWAYS AS IDENTITY PRIMARY KEY
# Dept_nome - varchar(255)

'''Atividade para casa:
Crie uma banco de dados de uma Biblioteca que deverá conter a seguinte tabela:

Livros:

Livro_id (PK)
Livro_nome
Livro_paginas
Livro_anoLançamento
Livro_autor (FK)

Autores:

Autor_id (PK)
Autor_nome

Conecte as duas tabelas usando a chave Livro_autor como chave estrangeira.
Dica: Se você já tiver criado a tabela Livros, use o comando ALTER

'''
def VerAutores(Todos=None):
    cursor.execute("""
    SELECT * FROM "Autor"
    """)
    Autores = cursor.fetchall()

    for autor in Autores:
        print(f'Id: {autor[0]}  Nome: {autor[1]}')
    if Todos==None:
        op=input('Procurar Livro   s/n\n').lower()
        match op:
            case 's':
                id=input('Autor id: ')
                VerLivros(id,autor[1])
            case 'n':
                pass

def VerLivros(id=None, nome=None):
    if id ==None:
        cursor.execute("""
        SELECT * FROM "Livros"
        """)
        Livros = cursor.fetchall()

        for livro in Livros:
            print(f'Id: {livro[0]}  Nome: {livro[1]} Paginas: {livro[2]} Lançamento: {livro[3]} Autor: {livro[4]}')
    else:
        cursor.execute(f"""
        SELECT * FROM "Livros" 
            WHERE "Autor" ='{id}'
        """)
        Livros = cursor.fetchall()

        for livro in Livros:
            print(f'Id: {livro[0]}  Nome: {livro[1]} Paginas: {livro[2]} Lançamento: {livro[3]} Autor: {nome}')
        
        
def AdicionarAutor():
    nome=f"'{input('Nome do Autor: ')}'"
    if nome== "''":
        nome='default'
    sql=f"""
    INSERT INTO "Autor"
    Values(default,{nome})
    """
    print(f'Nome : {nome}')
    return sql

def AdicionarLivro():
    VerAutores('Todos')
    AutId=f"'{input('Id Autor: ')}'"
    nome=f"'{input('Nome Do Livro: ')}'"
    paginas=f"'{input('Numero Do Paginas: ')}'"
    lançamento=f"'{input('Ano Do Lançamento: ')}'"
    
    for item in (nome,paginas,lançamento):
        if item=="''":
            item='default'
    sql=f"""
    INSERT INTO "Livros"("Autor","Livro_nome","Livro_paginas","Livro_anoLançamento")
    Values({AutId},{nome},{paginas},{lançamento})

     """

    return sql
while True:
    try:
        conn =psycopg2.connect(dbname="Empresa2",host="localhost",port="5432",user="postgres",password="postgres")
        cursor=conn.cursor()
        op=input("""    1-Ver Autores
        2-Ver Livros
        3-Adicionar Livros
        4-Adicionar Autor
        """)

        match op:
            case '1':
                VerAutores()
            case '2':
                VerLivros()
            case '3':
                cursor.execute(AdicionarLivro())
                conn.commit()
            case '4':
                cursor.execute(AdicionarAutor())
                conn.commit()
        

        cursor.close()
        conn.close()
    except(Exception,psycopg2.Error) as error:
        print("Não Conectado", error)











# conn =psycopg2.connect(dbname="Empresa2",host="localhost",port="5432",user="postgres",password="postgres")
# cursor=conn.cursor()




# cursor.execute("""
# CREATE TABLE "Livros"(
# "Livro_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
# "Livro_nome" varchar(255) NOT NULL default 'Não Informado',
# "Livro_paginas" int NOT NULL default 0,
# "Livro_anoLançamento" DATE NOT NULL default CURRENT_DATE,
# "Autor" int,
# CONSTRAINT "Livros_fkey" 
# FOREIGN KEY ("Autor")
#         REFERENCES  "Autor"("Autor_id")
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION
# )
#     """)

# conn.commit()