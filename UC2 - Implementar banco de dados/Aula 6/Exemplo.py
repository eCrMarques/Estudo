import psycopg2

conn = psycopg2.connect(dbname="Escola",host='localhost',port='5432', user='postgres', password= 'postgres')

cursor = conn.cursor()
Aluno='"Aluno"'
cursor.execute(f'''
Select * from {Aluno} order by "Cod_Matricula" asc
''')


print(cursor.description)
for aluno in cursor.fetchall():
    print(f'{aluno[0]}')
