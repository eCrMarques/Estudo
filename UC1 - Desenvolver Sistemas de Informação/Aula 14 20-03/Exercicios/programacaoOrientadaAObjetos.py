'''
Pesquise os seguintes assuntos:

Programação Orientada a Objetos em Python

Declaração de Classe em Python

Instaciando Objeto em Python

Encapsulamento em Python (Mais importante)

Herança em Python (Mais importante)

Polimorfismo em Python (Mais importante)

Utilize esses conhecimentos para resolver os seguintes problemas:

1. Crie uma classe Animal que tenha os atributos nome e idade e o método emitir_som(). 
Crie também as classes Cachorro, Gato e Pato que herdem da classe Animal e sobrescrevam o método emitir_som() para retornar “au au”, “miau” e “quack” respectivamente. 
Crie alguns objetos dessas classes e teste o método emitir_som() em cada um.
'''

class Animal:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade= idade

    def emitirsom(self,animal,som):
        if self.__idade==1:
            self.__idade=str(self.__idade)+' Ano'
        else:
            self.__idade=str(self.__idade)+' Anos'
        print(f'Sou um {animal}, Meu nome é {self.__nome}, tenho {self.__idade} e faço {som}')

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome,idade)

    def emitirsom(self):
        return super().emitirsom('Cachorro','Auau')

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        
    def emitirsom(self):
        return super().emitirsom('Gato','Miau')

class Pato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitirsom(self):
        return super().emitirsom('Pato','Quack')
print("\n---------------Questão 1-----------------")
cachorro1=Cachorro('Duke',4)
cachorro1.emitirsom()

gato1=Gato('Alfonso', 2)
gato1.emitirsom()

pato1=Pato('Elliot',1)
pato1.emitirsom()

'''
2. Crie uma classe Veiculo que tenha os atributos modelo, cor e ano e o método ligar(). 
Crie também as classes Carro, Moto e Bicicleta que herdem da classe Veiculo e sobrescrevam o método ligar() para imprimir “O carro está ligado”, 
“A moto está ligada” e “A bicicleta está pronta” respectivamente. Crie alguns objetos dessas classes e teste o método ligar() em cada um.
'''

class Veiculo:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def ligar(self):
        pass

class Carro(Veiculo):
    def __init__(modelo=None, cor=None, ano=None):
        super().__init__(modelo, cor, ano)

    def ligar(self):
        print('O carro está ligado')

class Moto(Veiculo):
    def __init__(self, modelo=None, cor=None, ano=None):
        super().__init__(modelo, cor, ano)
    
    def ligar(self):
        print('A moto está ligada')
    
class Bicicleta(Veiculo):
    def __init__(self, modelo=None, cor=None, ano=None):
        super().__init__(modelo, cor, ano)
    
    def ligar(self):
        print('A bicicleta está pronta')
    
print("\n---------------Questão 2-----------------")
carro1=Carro()
moto1=Moto()
bicicleta=Bicicleta()

carro1.ligar()
moto1.ligar()
bicicleta.ligar()

'''
3. Crie uma classe ContaBancaria que tenha os atributos privados numero, titular e saldo e os métodos públicos depositar(), sacar() e consultar_saldo(). 
O método depositar() deve receber como parâmetro a quantia a ser depositada e adicionar ao saldo. 
O método sacar() deve receber como parâmetro a quantia a ser sacada e subtrair do saldo, se houver saldo suficiente. O método consultar_saldo() deve retornar o valor do saldo. 
Crie um objeto dessa classe e teste os métodos.
'''

class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self.__numero=numero
        self.__titular=titular
        self.__saldo=saldo

    def depositar(self,valor):
        self.__saldo+=valor

    def sacar(self,valor):
        if self.__saldo>valor:
            self.__saldo-=valor
        else:
            print("Saldo Insuficiente")
    
    def consultarsaldo(self):
        return f'O Saldo equivale a: {self.__saldo}'

print("\n---------------Questão 3-----------------")

conta1=ContaBancaria(15465,'Funcionario',1454)
print(conta1.consultarsaldo())

conta1.depositar(100)
print(conta1.consultarsaldo())

conta1.sacar(600)
print(conta1.consultarsaldo())
    
'''
4. Crie uma classe Funcionario que tenha os atributos nome, salario e cargo e o método calcular_bonus(). 
Crie também as classes Gerente, Vendedor e Estagiario que herdem da classe Funcionario e sobrescrevam o método calcular_bonus() para retornar 20%, 10% e 5% do salário respectivamente.
Crie alguns objetos dessas classes e teste o método calcular_bonus() em cada um.
'''

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcularbonus(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, salario, cargo):
        super().__init__(nome, salario, cargo)

    def calcularbonus(self):
        return f'Cargo: {self.cargo}\nSalario: {self.salario}\nBonus: {self.salario*0.2}\n    --'
    
class Vendedor(Funcionario):
    def __init__(self, nome, salario, cargo):
        super().__init__(nome, salario, cargo)
    
    def calcularbonus(self):
        return f'Cargo: {self.cargo}\nSalario: {self.salario}\nBonus: {self.salario*0.1}\n    --'
    
class Estagiario(Funcionario):
    def __init__(self, nome, salario, cargo):
        super().__init__(nome, salario, cargo)
    
    def calcularbonus(self):
        return f'Cargo: {self.cargo}\nSalario: {self.salario}\nBonus: {self.salario*0.05}\n'


print("\n---------------Questão 4-----------------")
funcionario1=Gerente('Ana',2545,'Gerente')
funcionario2=Vendedor('Henrique',1454,'Vendedor')
funcionario3=Estagiario('Paulo',1214,'Estagiario')

print(funcionario1.calcularbonus())
print(funcionario2.calcularbonus())
print(funcionario3.calcularbonus())