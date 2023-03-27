class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca= marca
        self.modelo = modelo
        self.ano = ano
    
    def informacoes(self):
        return f'{self.marca} - {self.modelo} - {self.ano}'
    

    def acelerar(self, velocidade):
        print(f'O carro {self.marca} {self.modelo} acelerou para {velocidade} km/h')


Carro1=Carro('Fiat','Uno','2000')
print(Carro1.informacoes())
Carro1.acelerar(80)


class Agenda:
        def __init__(self, contatoMaximo, listaContatos=None):
            if listaContatos==None:
                 self.listaContatos=[]
            else:
                self.listaContatos = list(listaContatos)
            self.contatoMaximo = contatoMaximo

        def AdicionarContato(self, contato):
            if len(self.listaContatos)<self.contatoMaximo:
                self.listaContatos.append(contato)
            else:
                 print('Maximo de Contatos Atingido')
        
        def RemoverContato(self, contato):
            if contato in self.listaContatos:
                self.listaContatos.remove(contato)
            else:
                 print('Contato Não Encontrado')

        def Informacoes(self,):
             return self.listaContatos


class Contato:
     def __init__(self, nome, telefone):
          self.nome = nome
          self.telefone = telefone


Agenda1= Agenda(5)

Contato1= Contato('Emanuel','165464')
Contato2 = Contato('Cristian','654654')
print('Agenda')
print(Agenda1.Informacoes())

print('Adicionando Contato')
Agenda1.AdicionarContato(Contato1)
Agenda1.AdicionarContato(Contato2)

print('Agenda')
print(Agenda1.Informacoes())

print('Removendo Contato')
Agenda1.RemoverContato(Contato1)

print('Agenda')
print(Agenda1.Informacoes())

print('Nome e Dicionario')
print(Agenda1.listaContatos[0].nome)
print(Agenda1.listaContatos[0].__dict__)



# Problema: Crie uma classe chamada "Funcionario" que tenha como atributos o nome, o salário e a quantidade de faltas no mês. 
# Crie os métodos "aumentar_salario", que deve receber um valor e somá-lo ao salário atual, e 
# "descontar_falta", que deve receber um valor e subtraí-lo do salário, proporcionalmente à quantidade de faltas no mês (cada falta equivale a 1/30 do salário). 
# Além disso, crie o método "informacoes" que retorna uma string contendo o nome, o salário atual e a quantidade de faltas no mês.

class Funcionario:
     def __init__(self, nome, salario, faltas=None):
            if faltas==None:
               self.faltas=0
            else:
               self.faltas=faltas
            self.nome=nome
            self.salario=salario
    

     def aumentarsalario(self,valor):
        self.salario=self.salario+valor

     def descontarfalta(self,valor):
          valor=self.salario*(0.3*valor/10)
          self.salario=self.salario-valor


     def informacoes(self):
          return f'-----------Funcionario--------------\nNome: {self.nome}  \nSalario: {self.salario}  \nFaltas: {self.faltas}'

funcionario1= Funcionario('Cristian',1500)

print(funcionario1.informacoes())
funcionario1.aumentarsalario(100)
print(funcionario1.informacoes())
funcionario1.descontarfalta(30)
print(funcionario1.informacoes())


# Problema: Crie uma classe chamada "Pessoa" que tenha como atributos o nome, a idade e o peso. Crie também os métodos "comer",
# que deve receber um valor em gramas e adicionar ao peso da pessoa, e "envelhecer", que deve aumentar a idade em um ano e, se a idade for maior ou igual a 18, 
# aumentar o peso em 1 kg. Além disso, crie o método "informacoes" que retorna uma string contendo o nome, a idade e o peso atual.

class Pessoa:
    def __init__(self, nome, idade, peso):
         self.nome = nome
         self.idade = idade
         self.peso = peso

    def comer(self,valor):
         self.peso=self.peso+valor

    def envelhecer(self,valor):
         if self.idade>18:
              self.peso+=1
         self.idade=self.idade+valor
    def informacoes(self):
         return f'-----------Pessoa--------------\nNome: {self.nome}\n Idade: {self.idade}\n Peso: {self.peso}'


pessoa1=Pessoa('Emanuel',20,70)

print(pessoa1.informacoes())
pessoa1.comer(1)
print(pessoa1.informacoes())
pessoa1.envelhecer(1)
print(pessoa1.informacoes())

