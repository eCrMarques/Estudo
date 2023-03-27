class Funcionario:
    def __init__(self, nome, salario,cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        
    def dizerOla(self):

        print('Olá, meu nome é',self.nome)


funcionario1 = Funcionario('Jonas','+ de 8000','Assistente')

funcionario2 = Funcionario('Marcos',2000,'Vendedor')

print(funcionario1.nome)
print(funcionario1.salario)

funcionario1.dizerOla()
funcionario2.dizerOla()