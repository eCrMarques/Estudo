## Não tem nada Aqui --- Desculpa

## Não tem nada Aqui --- Desculpa

## Não tem nada Aqui --- Desculpa

## Não tem nada Aqui --- Desculpa

## Não tem nada Aqui --- Desculpa

## Não tem nada Aqui --- Desculpa

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def apresentar(self):
#         print(f"O meu nome é {self.nome}!")
#     def apresentar_idade(self):
#         print(f"A minha idade é {self.idade}!")

# pessoa = Pessoa("Maria", 30)
# pessoa.apresentar()
# pessoa.apresentar_idade()

# class Circulo:
#     def __init__(self, raio):
#         self.raio = raio
    
#     def area(self):
#         area = 3.14 * (self.raio**2)
#         return area
# circulo = Circulo(5)
# print(circulo.area())

# class Funcionario():
#     def __init__(self, nome, salario, departamento):
#         self.nome = nome
#         self.salario = salario
#         self.departamento = departamento

#     def aumentarSalario(self, salario):
#         self.salario = salario / 100 + self.salario
    
#     def informacoes(self):
#         print(f"{self.nome} - {self.departamento} - {self.salario}")


# pessoa = Funcionario("João", 3000, "Vendas")
# pessoa.informacoes()


class Agenda():
    def __init__(self,lista_de_contatos,n_cttpermitido ):
        self.listadecontato=lista_de_contatos
        self.n_cttpermitido= n_cttpermitido
    def Contato(self,contatos):
        self.contatos = contatos
