# 2. Classe Funcionário: Implemente a classe Funcionário. Um funcionário tem um
# nome e um salário. Escreva um construtor com dois parâmetros (nome e salário) e
# o método aumentarSalario (porcentualDeAumento) que aumente o salário do
# funcionário em uma certa porcentagem. Exemplo de uso: harry = f u n c i o n á r i o
# ( " H a r r y " , 2 5 0 0 0 ) harry.aumentarSalario(10) Faca um programa que teste o
# método da classe.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aumentarSalario(self,Percentual):
        salario= ((Percentual/100)*self.salario)+self.salario
        print(f'O Salario foi aumentado de {self.salario}R$ para {salario}R$')
        self.salario = salario

funcionario1= Funcionario('João',1200)
print(funcionario1.__dict__)

funcionario1.aumentarSalario(10)
print(funcionario1.salario)
print(funcionario1.__dict__)
